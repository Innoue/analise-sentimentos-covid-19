import csv
#Array para datas
months = ['Mar', 'Apr', 'May']
days = 32
contAll = 0
countPositive = 0
countNeutral = 0
countNegative = 0
polarity = 0
day = ''

#Abre o arquivo definido
file_name = 'tweets' 
extension = 'csv'
path_file_name = file_name + '.' + extension

for month in months:
  for i in range(1, days):
    if ((i - 9) <= 0):
      day = month + ' 0' + str(i)  
    else:
      day = month + ' ' + str(i)
    contAll = 0
    countPositive = 0
    countNeutral = 0
    countNegative = 0
    polarity = 0
    print(day)
    with open(path_file_name, 'r') as csvfile:
      plots = csv.reader(csvfile, delimiter = ',')
      next(plots, None)
      for row in plots:
        if (str(row[0]).find(day) != -1):
          contAll += 1
          polarity += float(row[1])
          if (float(row[1]) > 0):
            countPositive += 1
          elif (float(row[1]) < 0):
            countNegative += 1
          else:
            countNeutral += 1
    if(contAll > 0):
      with open('datasets/date_sentiment.csv', 'a', newline = '') as file:
        writer = csv.writer(file)
        writer.writerow([day, contAll, countPositive, countNeutral, countNegative, polarity])        
