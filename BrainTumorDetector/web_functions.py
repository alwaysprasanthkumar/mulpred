"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import streamlit as st
import joblib


@st.cache_data()
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('BrainTumorDetector/MRI.csv')

   
    # Perform feature and target split
    X = df[["AF3","F7","F3","FC5","T7","P7","O1","O2","P8","T8","FC6","F4","F8","AF4"]]
    y = df['result']

    return df, X, y

@st.cache_data()
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create the model
    model = RandomForestClassifier(
            n_estimators=200,  
            max_depth=10,
            min_samples_split=5,
            min_samples_leaf=1
        )
    # Fit the data on model
    model.fit(X_train, y_train)

    # Serialize and deserialize the trained model using joblib
    model = joblib.dump(model,"braintumor.joblib")
    return X_test, y_test


@st.cache_data
def load_model():
    """This function loads the trained model"""
    # Deserialize the trained model using joblib
    model = joblib.load("braintumor.joblib")
    return model

def predict(model,X_test,y_test, features):
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))

    # Get the model score
    score = model.score(X_test, y_test)

    return prediction,score
