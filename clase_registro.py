class Registro:
    __temperatura= float
    __humedad= float
    __presion= float
    
    def __init__(self,temperatura,humedad,presion):
        self.__temperatura= temperatura
        self.__humedad= humedad
        self.__presion= presion
    
    def getTemperatura(self):
        return float(self.__temperatura)
                
    def getVariables(self):
        return float(self.__temperatura), float(self.__humedad), float(self.__presion)