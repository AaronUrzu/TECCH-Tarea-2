# Complejidad temporal: O(1) para todas las operaciones (enQueue, deQueue, Front, Rear, isEmpty, isFull).
# Complejidad espacial: O(k) donde k es la capacidad máxima de la cola circular.
# Justificación: Se utiliza una lista de tamaño fijo pre-asignado y variables enteras 
# para rastrear el inicio y la cantidad de elementos. Al usar aritmética modular (%), 
# evitamos recorrer o redimensionar la lista, logrando que cada operación sea O(1).

class MyCircularQueue:
    def __init__(self, k: int):
        self.capacidad = k
        self.cola = [0] * k  # Lista de tamaño fijo
        self.inicio = 0      # Índice donde está el frente de la cola
        self.cantidad = 0    # Cuántos elementos hay actualmente en la cola

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Calculamos la posición del final usando aritmética modular
        fin = (self.inicio + self.cantidad) % self.capacidad
        self.cola[fin] = value
        self.cantidad += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # Movemos el inicio al siguiente elemento en el círculo
        self.inicio = (self.inicio + 1) % self.capacidad
        self.cantidad -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cola[self.inicio]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # Calculamos la posición del último elemento insertado
        fin = (self.inicio + self.cantidad - 1) % self.capacidad
        return self.cola[fin]

    def isEmpty(self) -> bool:
        return self.cantidad == 0

    def isFull(self) -> bool:
        return self.cantidad == self.capacidad