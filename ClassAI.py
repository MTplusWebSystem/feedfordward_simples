import numpy as np

class ChatIA:
    def __init__(self, entrada, frases, respostas):
        self.entrada = entrada
        self.frases = frases
        self.respostas = respostas
        self.palavras = set(' '.join(frases).lower().split())
        self.palavra_para_indice = {palavra: i for i, palavra in enumerate(self.palavras)}
        self.indice_para_palavra = {i: palavra for i, palavra in enumerate(self.palavras)}
        self.peso = np.random.rand(len(self.palavras))

    def ativador(self, x): 
        return 1 / (1 + np.exp(-x))
    
    def vetorizar(self):
        vetor = np.zeros(len(self.palavras))
        for palavra in self.entrada.lower().split():
            vetor[self.palavra_para_indice[palavra]] += 1
        return vetor 

    def main(self):
        while True:
            entrada = input(":")
            self.entrada = entrada
            self.frases = ['Olá','Qual seu nome?','Como você funciona?','Como você funciona?']
            self.respostas = ['Olá, tudo bem!','Meu codinome é ChatIA','Eu sou um algoritmo de aprendizagem com base no seu padrão de uso']
            self.palavras = set(' '.join(self.frases).lower().split())
            self.palavra_para_indice = {palavra: i for i, palavra in enumerate(self.palavras)}
            self.indice_para_palavra = {i: palavra for i, palavra in enumerate(self.palavras)}
            self.peso = np.random.rand(len(self.palavras))

            indice_resposta = self.ativador(np.dot(self.vetorizar(), self.peso))
            resposta = self.respostas[indice_resposta]
            print(resposta)


chat = ChatIA(None, [], [])
chat.main()