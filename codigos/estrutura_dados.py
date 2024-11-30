class ListaVetor:

    def __init__(self, tamanho_inicial=50):
        self.__vetor = [None for _ in range(tamanho_inicial)]
        self.__tamanho = 0

    def __len__(self):
        return len(self.__vetor)

    def __garante_capacidade(self):
        if self.__tamanho == len(self.__vetor):
            nova_lista = [None for _ in range(len(self.__vetor) * 2)]

            i = 0
            while i < self.__tamanho:
                nova_lista[i] = self.__vetor[i]

            self.__vetor = nova_lista


    def adicionar(self, valor):
        self.__garante_capacidade()
        self.__vetor[self.__tamanho] = valor

        self.__tamanho += 1

    def remover(self, indice):
        elemento = self.__vetor[indice]

        for i in range(indice, self.__tamanho - 1):
            self.__vetor[i] = self.__vetor[i + 1]


        self.__tamanho -= 1

        return elemento

    def __repr__(self):
        return f"Lista([{', '.join(repr(self.__vetor[i]) for i in range(self.__tamanho))}])"


class ListaLigada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0

    def __len__(self):
        return self.__tamanho

    def existe(self, elemento, no_atual = None):
        if no_atual is None:
            no_atual = self.__primeiro
        if no_atual.elemento == elemento:
            return True

        if no_atual.proximo is None:
            return False

        return self.existe(elemento, no_atual.proximo)

    def adicionar(self, elemento):
        novo_no =  ListaLigada.No(elemento)

        if self.__primeiro is None:
            self.__primeiro = novo_no
            self.__ultimo = self.__primeiro
        else:
            self.__ultimo.proximo = novo_no
            novo_no.anterior = self.__ultimo
            self.__ultimo = novo_no

        self.__tamanho += 1

    def remover(self, indice):
        if self.__primeiro is None:
            return -1

        if indice < 0:
            return -1

        i = 0
        atual = self.__primeiro
        anterior = self.__primeiro.proximo
        while atual:
            if i == indice:
                anterior.proximo = atual.proximo
                self.__tamanho -= 1
                return atual.elemento

            i += 1
            anterior = atual
            atual = atual.proximo


    def __iter__(self):
        atual = self.__primeiro
        while atual:
            yield atual.elemento
            atual = atual.proximo

    def __repr__(self):
        valores = [str(valor) for valor in self]
        return f"ListaLigada([{' -> '.join(valores)}])"

    class No:
        def __init__(self, elemento):
            self.elemento = elemento
            self.proximo = None


        def __repr__(self):
            return f'No({self.elemento})'
