import numpy as np

frases = ['Como você está?','Qual é seu nome?', 'O que você faz?', 'menu']
respostas = ['Estou bem, obrigado!', 'Meu nome é ChatIA', 'Eu sou um algoritimo com padrões especifico para te ajudar', '-'*20+'\n'+'[ 1 ] menu inicial']

def vetorizar(frase):
    vetor = np.zeros(len(palavras))
    for palavra in frase.lower().split():
        vetor[palavra_para_indice[palavra]] += 1
    return vetor

def ativador (x):
    return 1 / (1 + np.exp(-x))

correct_resposta = []
correct = "Como você está?"
while True:
    palavras = set(' '.join(frases).lower().split())
    palavra_para_indice = {palavra: i for i, palavra in enumerate(palavras)}
    indice_para_palavra = {i:palavra for i, palavra in enumerate(palavras)}

    entradas = np.array([[vetorizar(frase) for frase in frases]])  
    pesos = np.random.rand(len(palavras), len(respostas))
    mensagem = input(' exemplo: Como você está?: ')
    if len(correct_resposta) > 0 :
        for n in range(0,len(frases)):
            if frases[n] == mensagem:
                if n < len(correct_resposta): # Check if the index "n" is within the range of the list "correct_resposta"
                    print(correct_resposta[n])
                break
    saida = ativador(np.dot(vetorizar(mensagem), pesos))

    indice_reposta = np.argmax(saida)
    resposta_chat = respostas[indice_reposta]
    if correct != mensagem:
        correct_resposta.append(resposta_chat)
    print(resposta_chat)