
                                                                                # PART 1 #
# Importing relevant module

import pandas as pd
import numpy as np
from numpy.random import randint 
import seaborn as sns
import matplotlib.pyplot as plt
import requests,newsapi,pprint
import sqlalchemy
from sqlalchemy import create_engine
import sqlite3
from newsapi import NewsApiClient


newsapi = NewsApiClient(api_key='') # API key

# Using newsApi to streamline news Headline and Append the result into a Variable 
Title = [] # Contains the title headline
Description = [] # Contains the description headline
Sources = [] # Contains the sources headline
Url = [] # Contains the Url headline

top_headlines = newsapi.get_top_headlines(
    language='en')
for article in top_headlines['articles']:
    Title.append(article['title'])
    Description.append(article['description'])
    Sources.append(article['source']['name'])
    Url.append(article['url'])


# Convert the Variables into a DataFrame
news = pd.DataFrame({'source':Sources,'title':Title,'description':Description,'url':Url})

# View the dataFrame
news.head()

# Using the sqlalachemy module to create a Data_Base to dumb the dataFrame
engine = create_engine('sqlite:///C:\SQLiteStudio\DataBaseFolder\StreamLineNews.db',echo=False) # createEngine and naming the dataBase as "StreamLineNews"...
sqlite_connection = engine.connect()# Connecting to the data_Base


news.to_sql('NewsHeadLines',sqlite_connection,index=False,if_exists='replace') #Convet the News DataFrame into sql and Dumb into the "StreamLineNews" dataBase









                                                                            # PART 2 #
                                                                            
# Using Sqlite3 module to connect to the "StreamLineNews" dataBase
connection = sqlite3.connect('C:\SQLiteStudio\DataBaseFolder\StreamLineNews.db')
cur = connection.cursor()# Connecting to the dataBase

# Connecting to the Sqlite3 module using Pandas and
# Reading some columns from the "StreamLineNews" dataBase using Pandas
result = pd.read_sql_query('SELECT source,title,description FROM NewsHeadLines;',connection)



result.to_csv('News.csv',index=False)# Convert the result output to csv...







