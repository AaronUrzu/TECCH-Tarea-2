from collections import deque

# Complejidad temporal: O(n)
# Complejidad espacial: O(k)
# Justificación: Se recorre la lista nums una sola vez. Cada elemento se agrega 
# y se elimina de la cola a lo sumo una vez, haciendo que el tiempo sea lineal O(n). 
# La cola almacena como máximo k índices simultáneamente, por lo que el espacio es O(k). 
# Se utiliza collections.deque con append() y popleft() garantizando operaciones O(1).

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        resultado = []
        cola = deque()
        
        for i in range(len(nums)):
            # 1. Eliminar de la cola los índices que ya se salieron de la ventana actual
            if cola and cola[0] < i - k + 1:
                cola.popleft()
            
            # 2. Eliminar elementos menores al elemento actual por la derecha
            # (ya que nunca serán el máximo de esta ventana ni de las siguientes)
            while cola and nums[cola[-1]] < nums[i]:
                cola.pop()
                
            # 3. Agregar el índice del elemento actual
            cola.append(i)
            
            # 4. Si la ventana ya alcanzó el tamaño k, guardar el máximo (que está al frente)
            if i >= k - 1:
                resultado.append(nums[cola[0]])
                
        return resultado