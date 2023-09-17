import streamlit as st
import pickle
import pandas as pd 
def recommend(movie):
  movie_index = movies[movies['title'] == movie].index[0]
  distances = simarity_matrics[movie_index]
  movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  rec = []
  for i in movies_list:
    rec.append(movies.iloc[i[0]].title)
  return rec  
st.title("movie_recommender system")
movie_list = pickle.load(open('movie (1).pkl','rb'))
simarity_matrics = pickle.load(open('sim.pkl','rb'))
movies = pd.DataFrame(movie_list)
option = st.selectbox(
    'How would you like to be contacted?',
    movies['title'].values)
st.button("Recommend", type="primary")
if st.button(option):
    st.write(recommend(option))
