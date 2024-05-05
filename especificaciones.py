def está_explorado(t, inicio, fin):
    # Verificar si el segmento es una serie de componentes consecutivos
    if t[inicio:fin+1] != sorted(t[inicio:fin+1]):
        raise ValueError("El segmento no es una serie de componentes consecutivos.")

    # Encontrar el máximo componente en el segmento
    max_componente = max(t[inicio:fin+1])

    # Verificar si cada componente está colocado después del máximo
    for i in range(inicio, fin+1):
        if t[i] < max_componente:
            return False
    return True

# Ejemplo de uso
t = [3, 1, 4, 5, 2]
inicio = 1
fin = 3

resultado = está_explorado(t, inicio, fin)
print("¿El segmento está explorado?", resultado)
