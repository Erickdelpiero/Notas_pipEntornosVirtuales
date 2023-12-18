import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def millions_formatter(x, pos):
    return '%1.1fM' % (x * 1e-6)

def barras(labels, values, title='', ylabel=''):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    
    # Formateador para el eje Y en millones
    formatter = FuncFormatter(millions_formatter)
    ax.yaxis.set_major_formatter(formatter)
    
    plt.show()
    ##plt.savefig('pie.png')
    ##plt.close()

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