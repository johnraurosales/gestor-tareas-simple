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


while True:
    print("\nGestor de Tareas Simple")
    print("1. Crear tarea")
    print("2. Consultar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        tarea = input("Ingresa la tarea: ")
        agregar_tarea(tarea)
    elif opcion == "2":
        mostrar_tareas()
    elif opcion == "3":
        mostrar_tareas()
        num = int(input("Número de tarea a eliminar: "))
        eliminar_tarea(num)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
