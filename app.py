import streamlit as st
import requests
from PIL import Image
import pandas as pd

final_df = pd.read_pickle("movie_list.pkl")
similarity = pd.read_pickle("similarity.pkl")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=75eb0685f1f9140663e33eb0ea57150a&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie_name):
    movie_index = final_df[final_df["title"] == movie_name].index[0]
    distances = similarity[movie_index]
    index_list = list(enumerate(distances))
    similar_movie = sorted(index_list, reverse = True, key = lambda x: x[1])[1:11]
    
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in similar_movie:
        # fetch the movie poster
        movie_id = final_df.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(final_df.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters



image = Image.open('techma.png')

st.image(image, width=120)

st.header('Film Recommendation System')


movie_list = final_df['title'].values
selected_movie = st.selectbox(
    "Input the name of a movie or choose one from the provided list",
    movie_list
)

if st.button('Display The Recommendations'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.caption(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.caption(recommended_movie_names[1])
        

    with col3:
        st.image(recommended_movie_posters[2])
        st.caption(recommended_movie_names[2])
        
    with col4:
        st.image(recommended_movie_posters[3])
        st.caption(recommended_movie_names[3])
        
    with col5:
        st.image(recommended_movie_posters[4])
        st.caption(recommended_movie_names[4])

        
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[5])
        st.caption(recommended_movie_names[5])
    with col2:
        st.image(recommended_movie_posters[6])
        st.caption(recommended_movie_names[6])
        

    with col3:
        st.image(recommended_movie_posters[7])
        st.caption(recommended_movie_names[7])
        
    with col4:
        st.image(recommended_movie_posters[8])
        st.caption(recommended_movie_names[8])
        
    with col5:
        st.image(recommended_movie_posters[9])
        st.caption(recommended_movie_names[9])
    


