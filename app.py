import streamlit as st
import pickle
import pandas as pd
def recommend(movie):
   index = movies[movies['title'] == movie].index[0]
   distances = similarity[index]
   movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

   recommended_movie_names = []

   for i in movies_list:
      recommended_movie_names.append(movies.iloc[i[0]].title)
   return recommended_movie_names


movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity.pkl','rb'))
st.title("Movie Recommender System")

selected_movie_name= st.selectbox(
   "Select the movie to see recommendations..",
   movies['title'].values
)
if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

