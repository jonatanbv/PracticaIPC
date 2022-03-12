

class Nodo1:
    def __init__ (self, ingredientes=None, sig=None):
        self.ingredientes=ingredientes
        self.sig=sig

    def __str__(self):
        return '\t%s ' %(self.ingredientes)
        

class lista:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, elemento):
        if self.cabeza == None:
            self.cabeza = elemento
        if self.cola != None:
            self.cola.sig = elemento
        self.cola = elemento
    
    def listar(self):
        aux = self.cabeza
        while aux != None:
            print(aux)
            aux = aux.sig

