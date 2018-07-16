# use this app to run locally
#import dependencies
import os
import io
import numpy as np

import tensorflow as tf
import keras
from keras.preprocessing import image
from keras.models import load_model
from keras import backend as K

from flask import Flask, render_template, request, redirect, url_for, jsonify

#set up Flask
app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = 'tmp'
app.config['UPLOAD_FOLDER'] = 'static'
#get the current dictory name
MYDIR = os.path.dirname(__file__)
#set age to 0 to refresh image saved in the tmp folder
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#load fine tuned model
mymodel = load_model('my_model_final.h5')

#initiate tensorflow graph and session
graph = K.get_session().graph


#define a function to pre-process image
def prepare_image(img):
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = img / 255

    # return the processed image
    return img

#define index route
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    output = {"success": False}
    if request.method == 'POST':
        #if a file is selected and uploaded
        if request.files.get('file'):
            #read the file
            file = request.files['file']

            #specify the file name
            filename = 'upload.jpg'

            #create a path to the uploads folder
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            #filepath = os.path.join(MYDIR + "/" + app.config['UPLOAD_FOLDER'], filename)
            #save file
            file.save(filepath)

            #load the saved image using Keras and resize it to the format of 224x224 pixels
            image_size = (224, 224)
            im = image.load_img(filepath, target_size=image_size, grayscale=False)

            #preprocess the image and prepare it for classification
            processed_image = prepare_image(im)

            #define the list of flower names
            flower_list = ['daisy','dandelion','rose','sunflower','tulip']
            
            global graph
            with graph.as_default():
                #use the model to predict the preprocessed image
                predictions = mymodel.predict(processed_image)
                #get the index number of predictions
                predict_index = np.argmax(predictions, axis=1)[0]
                #use the index to look up the flower name from the list of flowers
                result = flower_list[predict_index]
                #extract the predict probabability/confidence number
                probability = float(predictions[0][predict_index])
                #save prediction results and probability to output dictionary
                output["flower"] = result
                output["probability"] = probability

                #indicate that the request was a success
                output["success"] = True

            #pass output to index html and render the page
            return render_template("index.html",result=output)


    return render_template("index.html",result='none')


if __name__ == "__main__":
    app.run(debug=True)