from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        """Inicialize sua estrutura aqui"""
        self.__itens = list()

    def __len__(self):
        """Aqui irá sua implementação"""
        return len(self.__itens)

    def enqueue(self, value):
        """Aqui irá sua implementação"""
        self.__itens.append(value)

    def dequeue(self):
        """Aqui irá sua implementação"""
        return self.__itens.pop(0)

    def search(self, index):
        """Aqui irá sua implementação"""
        if index not in range(len(self)):
            raise IndexError('Índice Inválido ou Inexistente')
        return self.__itens[index]
