# -*- coding: utf-8 -*-
"""streamlit_app.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wCfitPn6Az0rtP38HpCeCLpxPQVuBRyR
"""

# @title Setup code
# pip install streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py

# pip install pyngrok

# from google.colab import drive
# drive.mount('/content/drive')

import numpy as np
import pickle
import streamlit as st
import os

# yukarıdakileri fonkisyona alalım
def recommend_movie(movie):
  index = netflix_data_v2[netflix_data_v2['TITLE']==movie].index[0]
  # benzerlik değerlerine göre sıralayıp uzaklık değerine atıyoruz
  distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
  recommended_movies_name = []
  for index, _ in distance[:10]:
     index = netflix_data_v2.iloc[i[0]]['index']
     recommended_movies_name.append(netflix_data_v2['TITLE'])
  return recommended_movies_name

st.header("Netflix Movie Recommendation System")
# Get the full file path to 'netflix_titles.pkl'
file_path = os.path.abspath('netflix_titles.pkl')

# Load the file using the full path
netflix_data_v2 = np.load(file_path, allow_pickle=True)

movie_list = netflix_data_v2['TITLE'].values
select_movie = st.selectbox(
    "Please type or select a movie for recommendation",
    movie_list
)

if st.button("Show recommendation"):
    recommended_movies_name = recommend_movie(select_movie)

    # Display the recommended movie titles
    st.write("Recommended Movies:")
    for movie_name in recommended_movies_name:
        st.write(movie_name)
