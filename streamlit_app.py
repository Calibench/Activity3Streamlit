import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Enviroment_Temperature_change_E_All_Data_NOFLAG.csv')

st.title("Enviroment Temperatures")
st.write("[Dataset Link](https://www.kaggle.com/datasets/sevgisarac/temperature-change)")

