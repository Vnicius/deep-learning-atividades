import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import spline
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def weight_init(num_inputs, n_classes): 
    """
    Função que inicializa os pesos e bias aleatoriamente utilizando numpy
    Parâmetro: num_inputs - quantidade de entradas X
    Retorna: w,b - pesos e bias da rede inicializados
    """
    ### Insira seu código aqui (~2 linhas)
    w = np.random.random_sample((n_classes, num_inputs)) - 0.5
    b = np.random.random((n_classes,))
    return w,b

def activation_func(func_type, z):
    """
    Função que implementa as funções de ativação mais comuns
    Parãmetros: func_type - uma string que contém a função de ativação desejada
                z - vetor com os valores de entrada X multiplicado pelos pesos
    Retorna: saída da função de ativação
    """
    ### Seu código aqui (~2 linhas)
    if func_type == 'sigmoid':
        return 1/(1 + np.exp((-1) * z))
    elif func_type == 'tanh':
        return (np.exp(2 * z) - 1)/(np.exp(2 * z) + 1)
    elif func_type == 'relu':
        return z if z > 0 else 0
    elif func_type == 'degrau':
        return 1 if z > 0 else 0

# z = np.arange(-5., 5., 0.2)
# def visualizeActivationFunc(z):
#     z = np.arange(-5., 5., 0.2)
#     func = []
#     for i in range(len(z)):
#         func.append(activation_func('tanh', z[i]))

#     plt.plot(z,func)
#     plt.xlabel('Entrada')
#     plt.ylabel('Valores de Saída')
#     plt.show()
# visualizeActivationFunc(z)

def forward(w,b,X):
    """
    Função que implementa a etapa forward propagate do neurônio
    Parâmetros: w - pesos
                b - bias
                X - entradas
    """
    z = np.dot(X, w) + b
    out = activation_func('tanh', z)
    return out

def predict(out):
    """
    Função que aplica um limiar na saída
    Parâmetro: y - saída do neurònio
    """
    ### Seu código aqui (~1 linha)
    return 0 if out < 0.5 else 1
    #return [int(o * 10) for o in out]

def perceptron(x,y, num_interaction, learning_rate):
    """
    Função que implementa o loop do treinamento 
    Parâmetros: x - entrada da rede 
                y - rótulos/labels
                num_interaction - quantidade de interações desejada para a rede convergir
                learning_rate - taxa de aprendizado para cálculo do erro
    """
    #Passo 1 - Inicie os pesos e bias (~1 linha)
    w,b = weight_init(len(x[0]), len(y))
    #Passo 2 - Loop por X interações
    for _ in range(num_interaction):
        # Passo 3 -  calcule a saída do neurônio (~1 linha)
        y_pred = []
        for sample in x:
          saida = []
          for i in range(len(y)):
            saida.append(predict(forward(w[i], b[i], sample)))
          y_pred.append(saida)
        
        #print(y_pred)
        # Passo 4 - calcule o erro entre a saída obtida e a saída desejada nos rótulos/labels (~1 linha)
        erro = y - y_pred 
        # Passo 5 - Atualize o valor dos pesos (~1 linha)
        # Dica: você pode utilizar a função np.dot e a função transpose de numpy 
        w += np.dot(np.dot(erro, learning_rate), x)
        
    # Verifique as saídas
    print('Saída obtida:', y_pred)
    print('Pesos obtidos:', w)

    #Métricas de Avaliação
    # y_pred = predict(y_pred)
    # print('Matriz de Confusão:')
    # print(confusion_matrix(y, y_pred))
    # print('F1 Score:')
    # print(classification_report(y, y_pred))

# x = np.array([[0,0], [0,1], [1,0], [1,1]])
# y = np.array([0,0,0,1])

x = np.array([[0,0,0], [0,0,1], [0,1,0], [0,1,1], [1,0,0], [1,0,1], [1,1,0], [1,1,1]])
y = np.array([[1,0,0,0,0,0,0,0],
              [0,1,0,0,0,0,0,0],
              [0,0,1,0,0,0,0,0],
              [0,0,0,1,0,0,0,0],
              [0,0,0,0,1,0,0,0],
              [0,0,0,0,0,1,0,0],
              [0,0,0,0,0,0,1,0],
              [0,0,0,0,0,0,0,1]])

perceptron(x, y, 20000, 0.01)