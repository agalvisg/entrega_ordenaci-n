#CLASIFICACIÓN DE TAREAS

"""
Algoritmo de clasificación de tareas según restricciones.

    Ordena las distintas t's en función de sus restricciones, una debe de hacerse antes de la otra.
INPUT:
    - Lista de tareas.

OUTPUT:
    - Lista de tareas ordenadas.

PRECONDICIONES:
    -  Las tareas se ingresarán  en tuplas de 2 elementos, el primero será la tarea y el segundo la prioridad.

POSTCONDICIONES:
    - Se devolverá una lista con las tareas ordenadas según sus restricciones.    
"""
def topological_sort(tasks):
    # Step 1: Initialize variables
    in_degree = {task: 0 for task in tasks}
    adjacency_list = {task: [] for task in tasks}
    sorted_tasks = []

    # Step 2: Build the adjacency list and calculate in-degrees
    for task, priority in tasks:
        for prerequisite in priority:
            adjacency_list[prerequisite].append(task)
            in_degree[task] += 1

    # Step 3: Perform topological sorting
    queue = [task for task in tasks if in_degree[task] == 0]
    while queue:
        task = queue.pop(0)
        sorted_tasks.append(task)
        for prerequisite in adjacency_list[task]:
            in_degree[prerequisite] -= 1
            if in_degree[prerequisite] == 0:
                queue.append(prerequisite)

    # Step 4: Check for cycles
    if len(sorted_tasks) != len(tasks):
        return None  # There is a cycle in the graph

    return sorted_tasks


# Ejemplo
tasks = [('A', [1]), ('B', ['A']), ('C', ['A']), ('D', ['B', 'C']), ('E', ['D'])]
print(topological_sort(tasks))  # ['A', 'B', 'C', 'D', 'E']
