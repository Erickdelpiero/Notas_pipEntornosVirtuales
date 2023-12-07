import matplotlib.pyplot as plt

def barras(labels, values):
  fig, ax= plt.subplots()
  ax.bar(labels, values)
  plt.show()
  # plt.savefig('barras.png')
  # plt.close()

def torta(labels, values):
  fig, ax= plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis=('equal')
  plt.show()
  # plt.savefig('torta.png')
  # plt.close()

if __name__=='__main__':
  labels=['2022', '2020', '2015', '2010']
  values=[34049588, 33304756, 30711863, 29229572]
  barras(labels, values)
  torta(labels, values)