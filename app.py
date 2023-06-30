import pandas as pd
import numpy as np
import gradio as gd
# models use files 
import pickle 
# Visualization folders 
from PIL import Image
import matplotlib.pyplot as plt
# Scalers 
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import category_encoders as ce
from datetime import date

# Model 1
# gb
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 --GRADIO -- TEAM PARIS/src/gb.pkl', 'rb') as file:
    model1 = pickle.load(file)
# Model 2
# knn
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 --GRADIO -- TEAM PARIS/src/knn.pkl', 'rb') as file:
    model2 = pickle.load(file)
# Model 3
# logistic
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 --GRADIO -- TEAM PARIS/src/logistic.pkl', 'rb') as file:
    model3 = pickle.load(file)

#Import preprocessors 
#scaler 
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 --GRADIO -- TEAM PARIS/src/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)
#LabelEncoder
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 --GRADIO -- TEAM PARIS/src/label_encoder.pkl', 'rb') as file:
    le = pickle.load(file)
#Encoder
with open('C:/Users/user/Desktop/DESKTOP FOLDERS/ASSIGNMENTS/LP4 --GRADIO -- TEAM PARIS/src/encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)

# DEFINE FUNCTIONS 


# USER INPUT 
gr.Interface(
    fn=predict_churn,
    inputs=[gr.inputs.Dropdown(['Female', 'Male'], label='Gender'),
            gr.inputs.Dropdown(['Month-to-month', 'One year', 'Two year'], label='Contract'),
            gr.inputs.Dropdown(['DSL', 'Fiber optic', 'No'], label='Internet Service'),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="Online Security"),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="Online Backup"),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="Device Protection"),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="Tech Support"),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="TV Streaming"),
            gr.inputs.Radio(['Yes', 'No', 'No internet service'], label="Movie Streaming")],
    outputs=gr.outputs.Label(),
    title="Customer Churn Prediction App",
    description="Let's Get Started With Some Predictions!"
).launch()

