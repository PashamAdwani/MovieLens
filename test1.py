import pandas as pd
import numpy as np
from pandas.compat import StringIO

movies = pd.read_csv(r'D:\Data Analysis\Final Project\movies.dat', sep='::',index_col=0,header=None,engine='python')
#MovieID::Title::Genres


users = pd.read_csv(r'D:\Data Analysis\Final Project\users.dat', sep='::',index_col=0,header=None,engine='python')
#UserID::Gender::Age::Occupation::Zip-code


ratings = pd.read_csv(r'D:\Data Analysis\Final Project\ratings.dat', sep='::',index_col=0,header=None,engine='python')
#Ratings : UserID::MovieID::Rating::Timestamp


