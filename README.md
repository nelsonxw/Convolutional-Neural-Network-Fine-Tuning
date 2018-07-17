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
    + The result is very surprising.  All 10 modesl failed to predict dandelion, rose, sun flower and tulip, and scored 0 accuracy with these flowers.  The models scored between 75% and 85% when predicitng daisy.  
        <img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/pre-trained_model_comparison.PNG" width="400">
    + Used one of the models (Xception) to verify the predicted flower names under each category and it totally mis-predicted the names.  
[code link](https://github.com/nelsonxw/final_project/blob/master/2-verification_Xception.ipynb)  

2. Since all 10 models were trained with ImageNet pictures, decided to scraped pictures from ImageNet website and downloaded data for further validations.
    + Installed library from https://github.com/tzutalin/ImageNet_Utils, tweaked the codes to work for Python 3.  
    [code link](https://github.com/nelsonxw/Modified_ImageNet_Utils/tree/71287d9543cf939a62889c191aab7aea46876434)
    + Used the ID of flowers to download pictures
    + Used ImageNet images to predict flower names, and got same results.  
    [code link](https://github.com/nelsonxw/final_project/blob/master/3-verification_ImageNet.ipynb)

3. At this point, the only conclusion I can get is that the pre-trained models were traied to do other classifications, and cannot be used directly to predict the flower species I have.  However, these models can be fine-tuned and trained with my own data to classify the five different flower names.  Since InceptionResNetV2 scored the highest in step 1, I picked it for initial fine tuning.
    + Because it is very time consuming to run each epoch on my PC, I initially selected small training dataset with 50 pictures for each species to get a quick feel of the model.
    + When pre-processing the images, I used data augmentation function (rotate, shift, flip) to increase the amount of training data and reduce overfit.
    + I tweaked different parameters (# of layers to train, # of nodes in the new layer, drop out rate, batch size, optimizer, learning rate, # of epochs) and tried to improve prediction accuracy and reduce lose.  The accuracy keeps going up and reduction loss keeps going down in the training dataset with each epoch, however, the best result I could get from the validation dataset was only about 55%, with clear evidence of overfitting in the model.  
<img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/InceptionResNetV2_result1.PNG" width="300"> <img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/InceptionResNetV2_result2.PNG" width="300">
4. After some research, I learned that reducing the complexity of the network may reduce overfitting problems.  With that in mind, I compared the 10 models in terms how many layers do they have (more layers indicate more complexity).  It turned out VGG16 has the least amount of layers, so I switched to fine tune VGG16 model.
    + Complexity of each model  
        <img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/compare_model_complexity.PNG" width="400">  
        
        [code link](https://github.com/nelsonxw/final_project/blob/master/5-select_simple_model.ipynb)
    + Improved accuracy (75%) and lower reduction loss  
        <img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/VGG16_initial_result1.PNG" width="300"> <img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/VGG16_initial_result2.PNG" width="300">  
        [code link](https://github.com/nelsonxw/final_project/blob/master/6-finetune_model_VGG16.ipynb)
5. I tried to increase the learning rate by 3x in the hope of finding the global optimum quicker, but it ended up with more overfitting.  
    <img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/VGG16_worse_result1.PNG" width="300"> <img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/VGG16_worse_result2.PNG" width="300">  
    [code link](https://github.com/nelsonxw/final_project/blob/master/7-finetune_model_VGG16_2.ipynb)
6. I kept the learning rate at 0.00001, and in order to further reduce overfitting, I increased the amount of training data.  Increased from 50 pictures per species to 450 pictures per species.  The prediction accuracy improved to 85% with lower reduction loss.  
    <img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/VGG16_better_result1.PNG" width="300"> <img src="https://github.com/nelsonxw/final_project/blob/master/screen%20shots/VGG16_better_result2.PNG" width="300">  
    [code link](https://github.com/nelsonxw/final_project/blob/master/8-finetune_model_VGG16_3.ipynb)
    

7. I tested with differnet optimizer functions and settled on using Adam.  I used 100 pictures per species as validation dataset, and used all the remaining pictures from ImageNet (over 1000 pictures per species) as the training data.  The prediction accuracy improved to 95%.
    
