from listaIn import lista, Nodo1
import complemento

class Nodo:
    def __init__(self, nombre=None, id=None, cantidad=None, ingredientes=None, tiempo=None, tiempoPizzas=None, sig=None):
        self.nombre=nombre
        self.id = id
        self.tiempoPizzas = tiempoPizzas
        self.cantidad = cantidad
        self.ingredientes = ingredientes
        self.tiempo = tiempo
        self.sig = sig

    def __str__(self):
        print('nombre: %s \nTiempo Preparacion: %s \nCantidad de Pizzas:  %s' %(self.nombre, self.tiempoPizzas, self.cantidad))
        print('Ingredientes: ')
        self.ingredientes.listar()
        print('Orden incializada: ')
        complemento.mostrarTiempo(self.tiempo)
        return ''

class listaP:
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
        t=1
        if aux == None: 
            print('\nPor el momento no hay ordenes.\n')
        while aux != None: 
            print('\n========== Orden no. ', t, ' ==========\n')
            print(aux)
            t=t+1
            aux = aux.sig

    def mostrarActual(self, id):
        if int(self.cabeza.id) == int(id):
            print(self.cabeza)
            return self.cabeza.tiempo
        else:
            print('ya no cuentas con ordenes')
    
    def tiempoActual(self, id):
        if int(self.cabeza.id) == int(id):
            return self.cabeza.tiempoPizzas

    def eliminar(self, id):
        if int(self.cabeza.id) == int(id):
            self.cabeza = self.cabeza.sig
            return True
        else:
            aux = self.cabeza
            anterior = aux
            while aux != None:
                if int(aux.id) == int(id):
                    anterior.sig = aux.sig
                    return True
                anterior = aux
                aux = aux.sig
        return False

ls =listaP()


def menus():
    conteo = 0
    print('\n===========Restaurante lo mejor de la ciudad===========\n\n'+
          '               ------Bienvenido------\n'
    )

    while(True):
        print(
            '======================================================='+
            '\n1. Ordenes actuales\n'+
            '2. Crear orden\n'+
            '3. Entregar orden\n'+
            '4. Datos del Desarrollador\n'+
            '5. Salir\n'+
            '======================================================='
        )

        num = input('\nIngrese la opcion: ')
        print('')

        if num == '1':
            ls.listar()
            
        elif num == '2':

            nombre = input('ingrese el nombre: ')
            cantidad = input('ingrese la cantidad: ')
            listaIngredientes = lista()
            complemento.tiposPizza()
            tiempoPizzas = 0

            for i in range(int(cantidad)):
                opcion = input('ingrese los ingredientes: ')
                if opcion == '1':
                    ingredientes = 'Peperoni'
                    tiempoPizzas = tiempoPizzas + 3
                elif opcion == '2':
                    ingredientes = 'Salchicha'
                    tiempoPizzas = tiempoPizzas + 4
                elif opcion == '3':
                    ingredientes = 'Carne'
                    tiempoPizzas = tiempoPizzas + 10
                elif opcion == '4':
                    ingredientes = 'Queso'
                    tiempoPizzas = tiempoPizzas + 5
                elif opcion == '5':
                    ingredientes = 'Piña'
                    tiempoPizzas = tiempoPizzas + 2

                ingre = Nodo1(ingredientes)
                listaIngredientes.agregar(ingre)

            tiempo = complemento.horaInicio()
            id = 0
            nod = Nodo(nombre, id, cantidad, listaIngredientes, tiempo, tiempoPizzas)
            ls.agregar(nod)
            print('')
            conteo = conteo +1
            
        elif num == '3':
            if int(conteo) != 0:
                horas = 0
                minutos = 0
                print('========== Orden Entregada ===========\n')
                tiempo = ls.mostrarActual(0)
                tiempoFinal = complemento.horaFinal()
                print('hora de entrega: ')
                complemento.mostrarTiempo(tiempoFinal)
                print('')
                tiempoPreparacion = ls.tiempoActual(0)

                if tiempoPreparacion >= 60:
                    horas = (tiempoPreparacion//60)
                    minutos = (tiempoPreparacion%60)
                else:
                    minutos = tiempoPreparacion

                print('Tiempo total de preparacion: ')
                complemento.calcularHora(tiempo, tiempoFinal, horas, minutos)
                print('')

                ls.eliminar(0)
                conteo = conteo - 1
            else:
                print('\nYa no hay mas ordenes :D\n')
        elif num == '4':
            print('=========================================================================')
            print(
                '= Programa creado por: \tJONATAN JOSUE VASQUEZ PASTOR\n'+
                '= Carnet: \t\t202007092'+
                '\n= Carrera: \t\tIng. Ciencias y Sistemas'+
                '\n= Universidad: \t\tUNIVERSIDAD DE SAN CARLOS DE GUATEMALA USAC'
            )
            print('=========================================================================\n')

        elif num == '5':
            print('Vuelve pronto :D')
            exit()


if __name__ == '__main__':
    menus()
