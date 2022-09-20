from Academico.dominion.entidades import *


class Archivo:

    def getAllUsers(self, ruta):
        lista = []
        try:
            archivo = open(ruta, "r")
            for linea in archivo.readlines():
                tupla = linea.split(";")
                print(linea)
                obj = Usuario(tupla[0], tupla[1], tupla[2])
                lista.append(obj)
            archivo.close()
        except:
            print("Error de lectura!")
        return lista

    def getLogin(self, usu, clave, ruta):
        lista = self.getAllUsers(ruta)
        obj = None
        for i in range(len(lista)):
            print(lista[i].usuario, usu, clave)
            if usu == lista[i].usuario and clave == lista[i].clave:
                obj = lista[i]
                print("Verdadero", obj.usuario)
                break
        return obj
