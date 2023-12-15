import streamlit as st
import pickle
import requests
import os


from dotenv import load_dotenv
load_dotenv()


movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
movie_list = movies['title'].values
tmdb_api_token = os.environ['TMDB_API_TOKEN']

# def poster_fetcher(id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key={}".format(id,tmdb_api_token)
#     response = requests.get(url)
#     obj  = response.json()
#     return "https://image.tmdb.org/t/p/w500/" + obj['poster_path']



# def recommend(movie):
#     movie_names = []
#     posters = []
#     movie_index = movies[movies['title']==movie].index[0]
#     distance =  similarity[movie_index]
#     movie_list = sorted((list(enumerate(distance))),reverse=True,key=lambda x : x[1])[1:6]
#     for i in movie_list:
#         # movie_id = i[0]
#         movie_names.append(movies.iloc[i[0]].title)
#         posters.append(poster_fetcher(movies.iloc[i[0]].movie_id))
#     return movie_names,posters



# # st.title("movie recommendation system")
st.title(tmdb_api_token)

# selected_movie_name = st.selectbox("select any movie that you like",movie_list)

# if st.button('recommend'):
#     names,posters = recommend(selected_movie_name)
#     st.title("recommendations:")
#     # for (i,j) in zip(names,posters):
#     #     st.write(i)
#     #     st.image(j)


#     # col1, col2, col3, col4, col5 = st.columns(5)

#     # with col1:
#     #     st.text(names[0])
#     #     st.image(posters[0])

#     # with col1:
#     #     st.text(names[1])
#     #     st.image(posters[1])

#     # with col1:
#     #     st.text(names[2])
#     #     st.image(posters[2])

#     # with col1:
#     #     st.text(names[3])
#     #     st.image(posters[3])

#     # with col1:
#     #     st.text(names[4])
#     #     st.image(posters[4])

    

#     col = st.columns(len(names))[0]

# # Use a loop to add images horizontally
#     for (i,j) in zip(names,posters):
#         with col:
#             st.divider()
#             st.text(i)
#             st.image(j)


#     st.divider()
#     st.text('source - TMDB')







