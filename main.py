from clase_menu import Menu as M
from clase_registro import Registro as Reg
import csv

def leerArchivo():
    with open ("registro.txt") as archivo:
        reader= csv.reader(archivo,delimiter= ',')               
        for fila in reader:
            dia= int(fila[0])
            hora= int(fila[1])
            Un_registro= Reg(fila[2],fila[3],fila[4])
            tabla[dia-1][hora]= Un_registro

if __name__ == '__main__':
    filas= 5        #las filas representan los dias del mes
    columnas= 13    #las columnas representan las horas del dia
    tabla= [[0]*columnas for _ in range(filas)]
    menu= M(tabla,filas,columnas)
    leerArchivo()
    menu.generarMenu()
    
    
        
    
    
   
    
    