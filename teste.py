#Import das biblios
import os
import csv
from twarc import Twarc

#Chaves usadas para a API
consumer_key='IMJh4kjQLGDzUaT9t1v0RXm5Y'
consumer_secret='cjt9d684CpvElXof1BxUMgSakNnFBVLDweQTSpGZolzzrnU8JE'
access_token='968521944944529408-oI5NcJVaZellwrsPjhsQkQPDeAZJzKf'
access_token_secret='hc7bTI65fG97smD3ZEB6iCjLrBzHBxn2Sp6TIaX8fZSJZ'

#Criacao do objeto para hidratar os dados
t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

#Variaveris para armazenar os dados do dataset
tweet_id = []
total = []
contError = 0
contRetweet = 0
cont = 0

#Abre o arquivo definido
file_name = 'teste' 
extension = 'csv'
path_file_name = file_name + '.' + extension
with open(path_file_name, 'r') as csvfile:
  plots = csv.reader(csvfile, delimiter = ',')
  next(plots, None)
  for row in plots:
    for tweet in t.hydrate(["{:.0f}".format(float(row[0]))]):
        total.append([tweet['created_at'], row[1]])

print("Total Tweets   - ", cont)
print("Total Retweets - ", contRetweet)
print("Total Errors   - ", contError)
print (total)

#Arquivo de gravacao
with open('tweets.csv', 'a') as file:
  writer = csv.writer(file)
  for i in total:    
    writer.writerow(i)   
  writer.writerow([cont, contRetweet, contError])