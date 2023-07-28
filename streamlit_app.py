#IMPORT Streamlit
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#import our csv file
df = pd.read_csv("Enviroment_Temperature_change_E_All_Data_NOFLAG.csv")

#Create a page title for the page
#Emojis can be used as icons from https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Cereals!", page_icon=":bowl_with_spoon:", layout='wide')

with st.container():
    st.title("A Streamlit analysis demonstration using the Cereals Dataset!")
    st.write("[Dataset URL](https://www.kaggle.com/datasets/crawford/80-cereals)")
    st.write("[Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)")
    st.subheader("Below is the full dataset we will be using for our demonstration.")
    st.write(df)
st.write("------------------------------------------------------------------------------")



#A selection option for choosing desired cereal brand
#after selecting a cereal brand, information regarding brand is displayed onto the user
with st.container():
    st.subheader("Below is a Demonstration of a Suggestive Seach bar and a drop down menu for selecting elements from the dataset")
    st.title("Search Bar")
    search_term = st.text_input("Search for a cereal:", "")
    filtered_df = df[df["name"].str.contains(search_term, case=False)]
    st.write(filtered_df)

    st.title("Drop Down Menu")
    cereals_name = st.selectbox("Choose a Cereal Brand", df['name'].unique()) 
    cereal_info = df[df['name'] == cereals_name]
    st.write(cereal_info)
st.write("------------------------------------------------------------------------------")



#A barchart showing a comparison of calories between all brands and the descriptive statistics of calories
with st.container():
    st.title("Calories Comparison Descriptive Statistics")
    st.write(df['calories'].describe())
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(df["name"], df["calories"])
    ax.set_xlabel("Cereal")
    ax.set_ylabel("Calories")
    ax.set_title("Calories Comparison of Cereals")
    plt.xticks(rotation=90)
    st.pyplot(fig)
st.write("------------------------------------------------------------------------------")



with st.container():
    st.title("Interactive Scatter Plot to Compare Brand Rating")
    st.write(df['rating'].describe())
    
    
    selected_brands = st.multiselect("Select Cereal Brands", df["name"])
    filtered_df = df[df["name"].isin(selected_brands)]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(filtered_df["name"], filtered_df["rating"], c=filtered_df["rating"], cmap="coolwarm", alpha=0.7)
    ax.set_xlabel("Cereal Brand")
    ax.set_ylabel("Ratings")
    ax.set_title("Distribution of Ratings by Cereal Brands")
    plt.xticks(rotation=90)
    st.pyplot(fig)
st.write("------------------------------------------------------------------------------")



with st.container():
    st.title("A Youtube video embeded onto Streamlit!")
    youtube_url = "https://www.youtube.com/watch?v=VqgUkExPvLY&t=371s&ab_channel=CodingIsFun"
    st.video(youtube_url)
st.write("------------------------------------------------------------------------------")
