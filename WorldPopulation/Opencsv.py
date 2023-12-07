import csv

def read_csv(path):
  with open(path, 'r') as Filecsv:
    reader = csv.reader(Filecsv, delimiter=',')
    Head=next(reader)
    # print(Head)
    Archivo={}
    lista=[]
    for row in reader:
      Archivo = {key: value for key, value in zip(Head, row)}
      lista.append(Archivo)
    # print(lista)
  return lista

if __name__== '__main__':
  read_csv('Data.csv')