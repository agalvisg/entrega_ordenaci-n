"""
Algoritmo ordenamiento_dicotomía.

    # Ordena t mediante inserción dicotómica.

Input: Tabla t de n elementos: Int, Float, Str.

Output: Tabla t ordenada en orden ascendente.

precondición: t= [t1,t2,...,tn] y ti es elemento de t.
                'left' y 'right' son los extremos de la tabla, cuyos valores son 0 e i-1 respectivamente.
                'mid' es el punto medio de la tabla.

poscondición: t= [t1,t2,...,tn-1] y t1<=t2<=...<=tn-1.

"""


from typing import List, TypeVar

T = TypeVar('T', int, float, str) #Tipos de elementos en las listas

def ordenamiento_dicotomía(t:List[T]) -> None:
    """
    Ordena la lista t en orden ascendente por inserción dicotómica.

    
    :param t: Lista de elementos a ordenar
    
    :type t: List[T]

    """
    for i in range(0,len(t)):
        value = t[i]   
        left, right = 0, i -1

        #Busqueda dicotómica según value del elemento.

        while left <= right:
            mid = (left + right) // 2
            if value < t[mid]:
                right = mid - 1
            else:
                left = mid + 1

        #Desplaamiento de los elementos para insertar value en la posición correcta.

        for j in range(i, left, -1):
            t[j]= t[j-1]

        #insertar el valor en la posición correcta.

        t[left] = value


#ejemplo

lista = [7,3,4,1,6,3,9,8,0,4,6,5]

ordenamiento_dicotomía(lista)

print("La lista ordenada es: ", lista)
