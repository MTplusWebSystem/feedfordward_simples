import numpy as np

class ChatIA:
    def __init__(self, entrada):
        self.entrada = entrada
    def ativador(self, x): 
        return np.argmax(1 / (1 + np.exp(-x)))
    
    def vetorizar(self):
        vetor = np.zeros(len(self.palavras))
        for palavra in self.entrada.lower().split():
            if palavra in self.palavra_para_indice:
                vetor[self.palavra_para_indice[palavra]] += 1
        return vetor 

    def main(self):
        frases = ['Olá','Qual seu nome?','Como você funciona?','Como você funciona?']
        respostas = ['Olá, tudo bem!','Meu codinome é ChatIA','Eu sou um algoritmo de aprendizagem com base no seu padrão de uso']
        self.palavras = set(' '.join(frases).lower().split())
        self.palavra_para_indice = {palavra: i for i, palavra in enumerate(self.palavras)}
        self.indice_para_palavra = {i: palavra for i, palavra in enumerate(self.palavras)}
        self.peso = np.random.rand(len(self.palavras))

        indice_resposta = self.ativador(np.dot(self.vetorizar(), self.peso))
        resposta = respostas[indice_resposta]
        print(resposta)


while True:
    chat = ChatIA(input(":"))
    chat.main()