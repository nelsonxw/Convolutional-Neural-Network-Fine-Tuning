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
#app.config['UPLOAD_FOLDER'] = 'tmp'
app.config['UPLOAD_FOLDER'] = 'static'

MYDIR = os.path.dirname(__file__)
#set age to 0 to refresh image saved in the tmp folder
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

mymodel = load_model('my_model_final.h5')
graph = K.get_session().graph






@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return ("hello")


if __name__ == "__main__":
    # get port number of Heroku.  If not specified, default to 5000
    env_port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=env_port, debug=True)