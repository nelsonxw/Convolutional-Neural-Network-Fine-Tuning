# CNN Model Fine Tuning and Flower Classifications

### Problem Statement:  
What is an effective way to satify the curiosity of a five-year old kid?  When walking in a beautiful botanical garden with blooming flowers, how to utilize machine learning to help a human being learn the names of different flowers?

### Objective:

+ Compare 10 pre-trained Keras CNN models on their effectiveness in classifying flower types.
+ Pick the best pre-trained model and fine tune it to improve its prediction accuracy and achieve higher reductions in loss.
+ Create a simple web app where uses can upload pictures and find out the name of flowers

### Dataset:

+ Scrapped pictures of five species (daisy, dandelion, rose, sun flower and tulip) from ImageNet website for training and validation
+ Downloaded flower picture (same five species) dataset from Kaggle for testing

### Experiment Steps:
1. Downloaded initial data from Kaggle (https://www.kaggle.com/alxmamaev/flowers-recognition/home) and split it into training dataset and test dataset.  With the test dataset, directly applied the pre-trained CNN models to compare and pick which one works best in predicting the flower types.  
[code link](https://github.com/nelsonxw/final_project/blob/master/1-pretrained_models_comparison.ipynb)  
    + The result is very surprising.  All 10 modesl failed to predict dandelion, rose, sun flower and tulip, and scored 0 accuracy with these flowers.  The models scored between 70% and 80% on accuracy when predicitng daisy.
    + Used one of the models (Xception) to verify the predicted flower names under each category and it totally mis-predicted the names.  
[code link](https://github.com/nelsonxw/final_project/blob/master/2-verification_Xception.ipynb)  

    <img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/pre-trained_model_comparison.PNG" width="400">  

    

