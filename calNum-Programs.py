import math
import numpy as np

def func_fatorial(n):
  """ 
  Calcula o fatorial de um número n
  
  Arg: 
    n (int): número a ser calculado o fatorial
  
  Returns: 
    fat (int): fatorial de n
  """
  if n == 0:
    return 1

  fat = 1

  for i in range(n):
    fat = fat * (i + 1)

  return fat

def func_seno_aprox(x, n):
  """
    Calcula o seno de x através de uma série de Taylor

    Arg:
      x (float): valor a ser calculado o seno
      n (int): número de termos da série
    
    Returns:
      sen (float): valor do seno de x
  """
  sen = 0

  for i in range(n):
    sen += (((-1)**i) * (x**((2*i)+1))) / func_fatorial((2*i)+1)

  return sen

def func_cosseno_aprox(x, n):
  """
    Calcula o cosseno de x através de uma série de Taylor

    Arg:
      x (float): valor a ser calculado o cosseno
      n (int): número de termos da série  
    
    Returns:
      cos (float): valor do cosseno de x
  """
  cos = 0

  for i in range(n):
    cos += ((-1)**i) * (x**(2*i)) / func_fatorial(2*i)

  return cos

def func_exponecial_aprox_preci(precisao, x):
  """
    Calcula o valor de e^x através de uma série de Taylor até atingir uma precisão

    Arg:
      precisao (float): valor da precisão
      x (float): valor a ser calculado o exponencial
    
    Returns:
      a (int): número de termos da série
      e (float): valor do exponencial de x
  """
  e = 0
  a = 0
  while math.fabs(e - math.exp(x)) > precisao:
    e += x**a / func_fatorial(a)
    a += 1
  return a, e

def func_calcular_matriz(x, valores_x):
  """
    Calcula a matriz para a resolução de um polinômio para um valor x

    Arg:
      x (float): valor a ser calculado pelo polinômio
      valores_x (list): valores de x da interpolação

    Returns:
      matriz (np.array): matriz com os valores calculados
  """
  matriz = np.ones((len(valores_x),len(valores_x)))

  for i in range(len(valores_x)):
    for j in range(len(valores_x)):
      if i == j:
        matriz[i,j] = x - valores_x[i]
      else:
        matriz[i,j] = valores_x[j] - valores_x[i]

  return matriz

def func_calcular_resultado_polinomio_matriz(matriz, valores_x, valores_y):
  """
    Calcula o resultado do polinômio através da matriz por Lagrange

    Arg:
      matriz (np.array): matriz com os valores calculados
      valores_x (list): valores de x da interpolação
      valores_y (list): valores de y da interpolação

    Returns:
      resultado (float): resultado do polinômio
  """
  g_diagonal = 1
  g_coluna = 1
  g_soma = 0

  for i in range(len(valores_x)):
    for j in range(len(valores_x)):
      g_coluna = g_coluna * matriz[j,i]
      if i == j:
        g_diagonal  = g_diagonal * matriz[i,j]

    g_soma = g_soma + (valores_y[i]/g_coluna)
    g_coluna = 1

  return g_diagonal * g_soma

def func_resolucao_polinomio(var, intervalo, coeficientes):
  """
    Calcula o resultado do polinômio para um intervalo

    Arg:
      intervalo (list): intervalo de valores para calcular o polinômio
      coeficientes (list): coeficientes do polinômio

    Returns:
      nada
  """
  for i in range(intervalo[0],intervalo[1]+1):
    for j in range(1,len(coeficientes)):
        var = (i * var) + coeficientes[j]
    print(i, var)
    var = coeficientes[0]

def main():
  print(func_fatorial(5))
  print(func_seno_aprox(3.14, 10))
  print(func_cosseno_aprox(3.14, 10))
  print(func_exponecial_aprox_preci(0.0001, 1))
  print(func_calcular_matriz(0.5, [0, 1, 2]))
  print(func_calcular_resultado_polinomio_matriz(func_calcular_matriz(0.5, [0, 1, 2]), [0, 1, 2], [0, 1, 4]))
  func_resolucao_polinomio(0,[0, 5], [1, 2, 3, 4])
  
main()