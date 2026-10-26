# Complejidad temporal: O(1) amortizado para push, pop, peek y empty.
# Complejidad espacial: O(n) donde n es el número de elementos en la cola.
# Justificación: Se usan dos listas como pilas. Los elementos se mueven de la 
# pila de entrada a la de salida solo cuando la de salida está vacía, haciendo 
# que las operaciones pop/peek sean O(1) en promedio.

class MyQueue:
    def __init__(self):
        # Inicializamos dos listas para simular las pilas
        self.pila_entrada = []
        self.pila_salida = []

    def push(self, x: int) -> None:
        # Encolar es simplemente agregar a la pila de entrada
        self.pila_entrada.append(x)

    def pop(self) -> int:
        # Para desencolar, necesitamos que los elementos estén en la pila de salida
        self.peek() # Reutilizamos la lógica de peek para mover los elementos si es necesario
        return self.pila_salida.pop()

    def peek(self) -> int:
        # Si la pila de salida está vacía, pasamos todos los elementos de la entrada a la salida
        if not self.pila_salida:
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        # Retornamos el tope de la pila de salida (el frente de nuestra cola)
        return self.pila_salida[-1]

    def empty(self) -> bool:
        # Está vacía solo si ambas pilas están vacías
        return not self.pila_entrada and not self.pila_salida