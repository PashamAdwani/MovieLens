import pandas as pd
import numpy as np
import imp
from pandas.compat import StringIO
from sklearn.model_selection import train_test_split

movies = pd.read_csv(r'D:\Data Analysis\Final Project\movies.dat', sep='::',index_col=False,header=None,engine='python')
movie_id=movies[0]
movie_genre=movies[2]
unique_genre=movie_genre.unique()
x=enumerate(unique_genre)

users = pd.read_csv(r'D:\Data Analysis\Final Project\users.dat', sep='::',index_col=False,header=None,engine='python')

ratings = pd.read_csv(r'D:\Data Analysis\Final Project\ratings.dat', sep='::',index_col=False,header=None,engine='python')

ratings_red=ratings.iloc[1:50000,:]

label=ratings_red[2]

data=ratings_red[0:1]

sz_users=users.shape[0]
sz_movies=movies.shape[0]
rat_user_id=ratings_red[0]
rat_movie_id=ratings_red[1]

#enumerate the genres



genre_data=np.zeros((50000,1))


##
##for i in range(50000):
##    for j in range(sz_movies):
##        if(rat_movie(i)==movie_id(j)):
##            genre_data(i)=



