#Import das biblios
import os
import csv
from twarc import Twarc

#Chaves usadas para a API
consumer_key='xxxxxxxxxx'
consumer_secret='xxxxxxxxxx'
access_token='xxxxxxxxxx'
access_token_secret='xxxxxxxxxx'

#Criacao do objeto para hidratar os dados
t = Twarc(consumer_key, consumer_secret, access_token, access_token_secret)

#Variaveris para armazenar os dados do dataset
tweet_id = []
total = []
contError = 0
contRetweet = 0
cont = 0
contNotUs = 0
contall = 0
errorid = 0

#Abre o arquivo definido
file_name = 'tweets_id_sentiment' 
extension = 'csv'
path_file_name = file_name + '.' + extension
with open(path_file_name, 'r') as csvfile:
  plots = csv.reader(csvfile, delimiter = ',')
  next(plots, None)
  for row in plots:
    contall += 1 #Contabiliza o total de tweets analisados
    #Tenta converter para eliminar a notacao cientifica
    try:
      id = ("{:.0f}".format(float(row[0])))
    except:
      errorid += 1
    #Hidrata o tweet a partir de seu ID
    try:
      for tweet in t.hydrate([int(id)]):
        if (tweet['place']['country_code'] == 'US'):      #Verifica se é o pais US
          if (tweet['full_text'].find('RT', 0, 3) == -1): #Verifica se não é um RT
            cont = cont + 1                               #Contabiliza os dados que deram certo
            #Abre e registra o arquivo
            with open('datasets/tweets.csv', 'a', newline='') as file:  
              writer = csv.writer(file)  
              writer.writerow([tweet['created_at'], row[1]])   
          else:
            contRetweet = contRetweet + 1 
        else:
          contNotUs += 1
    except:
      contError = contError + 1
    print(contall, ' - US =', cont, ' - RT =', contRetweet,' - NotUS =', contNotUs,' - Error =' ,contError,' - ErrorID =' ,errorid,'\n')

print("Total Tweets   - ", cont)
print("Total Retweets - ", contRetweet)
print("Total Errors   - ", contError)
print("Total Not US   - ", contNotUs)
print("Cont all - ", contall)

#Arquivo de gravacao
with open('datasets/tweets.csv', 'a', newline='') as file:
  writer = csv.writer(file)
  
  writer.writerow(['contall', 'cont', 'contRetweet', 'contNotUs', 'contError'])  
  writer.writerow([contall, cont, contRetweet, contNotUs, contError])
