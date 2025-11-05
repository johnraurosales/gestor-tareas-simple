tareas = []


def agregar_tarea(tarea):
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")


def mostrar_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        print("Listado de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")


def eliminar_tarea(num):
    if 0 < num <= len(tareas):
        tarea = tareas.pop(num - 1)
        print(f"Tarea '{tarea}' eliminada.")
    else:
        print("Número de tarea inválido.")
