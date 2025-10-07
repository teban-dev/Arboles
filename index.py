# Clase Nodo
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = [] 

class Arbol:
    def __init__(self):
        self.raiz = None
    
    def crear_arbol(self):
        dato_raiz = input("Ingrese el valor de la raíz: ")
        self.raiz = Nodo(dato_raiz)
        self._agregar_hijos(self.raiz)

    def _agregar_hijos(self, nodo):
        while True:
            resp = input(f"¿El nodo '{nodo.dato}' tiene hijos? (s/n): ").lower()
            if resp == 's':
                cant = int(input(f"¿Cuántos hijos tiene '{nodo.dato}'?: "))
                for i in range(cant):
                    hijo_dato = input(f"Ingrese el valor del hijo {i+1} de '{nodo.dato}': ")
                    nuevo_hijo = Nodo(hijo_dato)
                    nodo.hijos.append(nuevo_hijo)
                    self._agregar_hijos(nuevo_hijo)
                break

            elif resp == 'n':
                break

            else:
                print("Respuesta inválida, use 's' o 'n'.")

    def peso(self):
        return self._contar_nodos(self.raiz)

    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        total = 1  
        for hijo in nodo.hijos:
            total += self._contar_nodos(hijo)
        return total

    def orden(self):
        return self._orden(self.raiz)

    def _orden(self, nodo):
        if nodo is None:
            return 0
        max_hijos = len(nodo.hijos)
        for hijo in nodo.hijos:
            max_hijos = max(max_hijos, self._orden(hijo))
        return max_hijos

    def altura(self):
        return self._altura(self.raiz)

    def _altura(self, nodo):
        if nodo is None:
            return 0
        if not nodo.hijos:
            return 1
        return 1 + max(self._altura(h) for h in nodo.hijos)

#Esto de aca es el main basicamente xd
if __name__ == "__main__":
    arbol = Arbol()
    arbol.crear_arbol()

    print("\nFINAL:")
    print(f"Peso del árbol: {arbol.peso()}")
    print(f"Orden del árbol: {arbol.orden()}")
    print(f"Altura del árbol: {arbol.altura()}")
