import streamlit as st
import pandas as pd
import pickle

# Load and process data (copy this from your notebook)
# movies = pd.read_csv('tmdb_5000_movies.csv')
# credits = pd.read_csv('tmdb_5000_credits.csv')
movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# Your preprocessing and similarity function here...

def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(distances)) , reverse = True , key = lambda x:x[1])[1:7]

    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies    

# Streamlit UI
st.title("🎬 Movie Recommender System")

movie_list = movies['title'].values
selected_movie = st.selectbox("Choose a movie", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    st.subheader("Top Recommendations:")
    for i in recommendations:
        st.write(i)
