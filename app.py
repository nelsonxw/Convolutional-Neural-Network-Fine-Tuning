import os
import io
import numpy as np

import tensorflow as tf
import keras
from keras.preprocessing import image
from keras.models import load_model
from keras import backend as K

from flask import Flask, render_template, request, redirect, url_for, jsonify


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'
app.config['UPLOAD_FOLDER_MODEL'] = 'upload_models'

WORKING_FOLDER = os.path.dirname(__file__)

#set age to 0 to refresh image saved in the tmp folder
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

mymodel = None
graph = K.get_session().graph


def prepare_image(img):
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255

    # return the processed image
    return img


def save_file(request, filename, config_folder):
    if request.files.get('file'):
        filepath = os.path.join(app.config[config_folder], filename)
        file = request.files['file']
        file.save(filepath)
        return filepath
    else:
        return None


def reload_model(name):
    global mymodel
    global graph
    with graph.as_default():
        mymodel = load_model('upload_models/{}'.format(name))


@app.route('/model_upload', methods=['GET', 'POST'])
def model_upload():
    if request.method == 'GET':
        return render_template("model_upload.html", result='')
    else:
        if request.form.get('secret', "") == 'mySecretCode984736':
            save_file(request, 'my_model_final.h5', 'UPLOAD_FOLDER_MODEL')
            reload_model('my_model_final.h5')
            return render_template("model_upload.html",
                    result='Model reloaded.', msg='Ready to predict!')
        else:
            return render_template("model_upload.html", result='Bad secret code.')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    output = {"success": False}
    if request.method == 'POST':
        if request.files.get('file'):

            filepath = save_file(request, 'upload.jpg', 'UPLOAD_FOLDER')

            # Load the saved image using Keras and resize it to the Xception
            # format of 299x299 pixels
            image_size = (224, 224)
            im = image.load_img(filepath, target_size=image_size, grayscale=False)

            # preprocess the image and prepare it for classification
            processed_image = prepare_image(im)

            flower_list = ['daisy','dandelion','rose','sunflower','tulip']

            global graph
            with graph.as_default():
                predictions = mymodel.predict(processed_image)
                predict_index = np.argmax(predictions, axis=1)[0]

                result = flower_list[predict_index]
                probability = float(predictions[0][predict_index])

                output["flower"] = result
                output["probability"] = probability

                # indicate that the request was a success
                output["success"] = True

            return render_template("index.html",result=output)


    return render_template("index.html",result='none')


if __name__ == "__main__":
    # get port number of Heroku.  If not specified, default to 5000
    env_port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=env_port, debug=True)
