class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self,color):
        colores=["rojo","verde","amarillo","negro","blanco"]
        if color in colores:
            self.color=color
        
class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo 
        self.registro = registro

    def cambiarRegistro(self,registro):
        self.registro = registro

    def asignarTipo(self,tipo):
        tipos=["gasolina","electrico"]
        if tipo in tipos:
            self.tipo=tipo

class Auto:
    cantidadCreados=0;
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        c=0
        for i in self.asientos:
            if i!=None:
                c+=1
        return c

    def verificarIntegridad(self):
        for i in self.asientos:
            if i!=None:
                if i.registro!= self.registro:
                    return "Las piezas no son originales"
        if self.registro == self.motor.registro:
            return "Auto original"
        else:
            return "Las piezas no son originales"


