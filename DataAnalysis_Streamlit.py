# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 10:41:19 2022

@author: Sai Amujala

Instrunctions:
    streamlit run C:/Users/HCE8168/Desktop/Python/DSLearning/Projects/DataAnalysis_Streamlit.py 

"""

import pandas as pd
import seaborn as sns
import streamlit as st


# Adding Title & Subheader
st.title("Data Analysis")
st.subheader("Data Analysis using Python & Streamlit")

# Upload dataset

upload = st.file_uploader("Upload your dataset (in csv format)")
if upload is not None:
    data=pd.read_csv(upload)

# Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())

# Check Dataset of each column
# we might encounter an error with dtype. to resolve set global.dataframeSerliazation to legacy
# run this command in prompt  (streamlit run C:/Users/HCE8168/Desktop/Python/DSLearning/Projects/DataAnalysis_Streamlit.py --global.dataFrameSerialization legacy)

if upload is not None:
    if st.checkbox("Datatype of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)
        
# Check Shape of the dataset

if upload is not None:
    if st.checkbox("Shape of the dataset"):
        st.text("No.of rows: ")
        st.write(data.shape[0])
        st.text("No.of columns: ")
        st.write(data.shape[1])

# Check null values in dataset
# we might encounter a warning and it can be reolsved by adding following line in the code before st.pyplot()
# st.set_option('deprecation.showPyplotGlobalUse', False)

if upload is not None:
    data_missing = data.isnull().values.any()
    if data_missing==True:
        if st.checkbox("Null values in the dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("Congratulations!! No missing values")

# Check Duplicate values in the dataset        
if upload is not None:
    dup = data.duplicated().any()
    if dup==True:
        st.warning("This dataset has duplicate values")
        remove = st.selectbox("Do you want to Remove Duplicate values?",\
                              ("Select an option: ","Yes","No"))
        if remove=="Yes":
            data=data.drop_duplicates()
            st.text("Duplicate vaues are removed!!")
        if remove=="No":
            st.text("OK! No problem")

# Get Overall stats
if upload is not None:
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe(include='all'))

# About App

if st.button("About App"):
   st.text("Built with Streamlit") 
   st.text("Created by Sai") 
   
           
            

