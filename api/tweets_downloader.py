"""
Autor: @pythonistabr
data: 23-06-2022
"""

from pandas import DataFrame
import snscrape.modules.twitter as sntwitter

    
def create_queries(set_of_restaurants: set, set_of_emojis: set) -> list:
  queries = []
  
  for restaurant in set_of_restaurants:
    for emoji in set_of_emojis:
      queries.append(f"{restaurant} {emoji}")
  
  return queries



def search(limit: int, list_of_queries: list) -> list:
  tweets = []
  
  for query in list_of_queries:
    for tweet in sntwitter.TwitterSearchScraper(query + " lang:pt").get_items():
      if len(tweets) >= limit:
        break;  
      tweets.append({"date":tweet.date, "user_name" :tweet.user.username,
               "tweet":tweet.content})
  
  return tweets



def create_data_frame(dados: list) -> DataFrame:
  texto, nome_usuario, data_publicacao = [], [], []
  
  for tweet in dados:
    texto.append(tweet["tweet"].replace("\t", ""))
    data_publicacao.append(tweet["date"])
    nome_usuario.append(tweet["user_name"])
  
  main_data = DataFrame({"user_name":nome_usuario, "tweet":texto,
               "date":data_publicacao})
  
  return main_data