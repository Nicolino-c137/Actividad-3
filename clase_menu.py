import sys, os

class Menu:
    __elecciones= {}
    __tabla= None
    __filas= int
    __columnas= int
    
    def __init__(self, tabla,filas,columnas):
        self.__tabla= tabla
        self.__filas= filas
        self.__columnas= columnas
        self.__elecciones= {
            '1': self.opcion1,
            '2': self.opcion2,
            '3': self.opcion3,
            '0': self.salir
        }
        
    def mostrarMenu(self):
        print("""
MENU PRINCIPAL

1. Mostrar para cada variable metereológica el día y hora de menor y mayor valor
2. Mostrar la temperatura promedio mensual por cada hora
3. Listar los valores de las variables metereológicas 
0. Salir
""")
        
    def generarMenu(self):
        while True:
            self.mostrarMenu()
            op= input("Seleccion alguna opción: ")
            os.system("cls")
            ejecutar= self.__elecciones.get(op)
            if ejecutar:
                ejecutar()
            else: 
                print("Opcion no valida, vuelva a intentarlo")
                os.system("pause")
                os.system("cls")
            
    def opcion1(self):
        print("1. Mostrar para cada variable metereológica el día y hora de menor y mayor valor")
        max_temp= -11111
        max_hum= -11111
        max_pres= -11111
        min_temp= 99999
        min_hum= 99999
        min_pres= 99999
        for i in range(self.__filas):
            for j in range(self.__columnas):
                temperatura, humedad, presion= self.__tabla[i][j].getVariables()
                if temperatura > max_temp:
                    max_temp= temperatura
                    dia_maxT= i
                    hora_maxT= j
                if temperatura < min_temp:
                    min_temp= temperatura
                    dia_minT= i
                    hora_minT= j
                if humedad > max_hum:
                    max_hum= humedad
                    dia_maxH= i
                    hora_maxH= j
                if humedad < min_hum:
                    min_hum= humedad
                    dia_minH= i
                    hora_minH= j
                if presion > max_pres:
                    max_pres= presion
                    dia_maxP= i
                    hora_maxP= j
                if presion < min_pres:
                    min_pres= presion
                    dia_minP= i
                    hora_minP= j
        print(f"""
A las {hora_maxT}hs del dia {dia_maxT+1} se registró la mayor temperatura
A las {hora_minT}hs del dia {dia_minT+1} se registró la menor temperatura
A las {hora_maxH}hs del dia {dia_maxH+1} se registró la mayor humedad
A las {hora_minH}hs del dia {dia_minH+1} se registró la menor humedad
A las {hora_maxP}hs del dia {dia_maxP+1} se registró la mayor presión
A las {hora_minP}hs del dia {dia_minP+1} se registró la menor presión""")
        os.system("pause")
           
    def opcion2(self):
        print("2. Mostrar la temperatura promedio mensual por cada hora")
        for j in range(self.__columnas):
            cont= 0
            for i in range(self.__filas):
                cont+= self.__tabla[i][j].getTemperatura()
            prom= cont/self.__filas
            print(f"La temperatura promedio mensual es de {prom:.1f}°C para las {j}hs")                
        os.system("pause")
    
    def opcion3(self):
        print("3. Listar los valores de las variables metereológicas ")
        dia= int(input("Ingrese un día para ver las variables metereológicas por hora: "))
        print(f"\nAsí estuvo el clima el dia {dia}:")
        for j in range(self.__columnas):
            temp,humedad,presion= self.__tabla[dia-1][j].getVariables()
            print(f"""
Hora    Temperatura     Humedad     Presión
 {j}         {temp}          {humedad}       {presion}""")
        os.system("pause")
    
    def salir(self):
        sys.exit(0)