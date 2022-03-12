import time
import datetime
from tabulate import tabulate


def horaInicio():
    ahora = datetime.datetime.now()
    horaInicio = ahora.hour
    minutoInicio = ahora.minute
    segundoInicio = ahora.second
    return [horaInicio, minutoInicio, segundoInicio]
    
    
def horaFinal():
    ahora = datetime.datetime.now()
    horaFinal = ahora.hour
    minutoFinal = ahora.minute
    segundoFinal = ahora.second
    return [horaFinal, minutoFinal, segundoFinal]

def calcularHora(inicio, final, hora, minutos):
    
    tiempoFinal = [[final[0] - inicio[0] + hora, final[1] + minutos - inicio[1], abs(final[2] - inicio[2])]]

    print(tabulate(tiempoFinal, headers=["Horas", "Minutos", "Segundos"]))

def mostrarTiempo(tiempo):
    tiempo =[tiempo]
    print(tabulate(tiempo, headers=["Hora", "Minutos", "Segundos"]))

def tiposPizza():
    d = [
        [1,"peperoni", '3 min'],
        [2,'Salchicha', '4 min'],
        [3, 'Carne', '10 min'],
        [4, 'Queso', '5 min'],
        [5, 'Piña', '2 min']
    ]
    print('')
    print(tabulate(d, headers=["Opcion", "Ingrediente", "Tiempo"]))
    print('')









    

