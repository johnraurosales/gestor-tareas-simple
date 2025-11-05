# gestor_tareas_simple.py
# Un gestor de tareas por consola, simple, para practicar Python y Git.

# Lista global donde se almacenan las tareas pendientes
tareas = []


def agregar_tarea(tarea):
    """
    Agrega una tarea nueva a la lista si no está vacía.
    Muestra un mensaje si el usuario intenta agregar una tarea vacía.
    """
    if tarea.strip() == "":
        print("❌ La tarea no puede estar vacía.")
    else:
        tareas.append(tarea)
        print("\n✅ ¡Tarea agregada exitosamente!")


def mostrar_tareas():
    """
    Muestra el listado de tareas pendientes.
    Si no hay tareas, muestra un mensaje invitando a crear una nueva.
    """
    if not tareas:
        print("\n📋 No hay tareas pendientes. ¡Agrega una nueva!")
    else:
        print("\n📝 Listado de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")


def eliminar_tarea(num):
    """
    Elimina la tarea indicada por el usuario.
    Si el número no corresponde a una tarea existente, muestra un mensaje de advertencia.
    """
    if 0 < num <= len(tareas):
        tarea = tareas.pop(num - 1)
        print(f"\n🗑️ Tarea '{tarea}' eliminada correctamente.")
    else:
        print("\n⚠️ Número de tarea inválido. Intenta otra vez.")


# Bucle principal: Menú interactivo de la aplicación
while True:
    print("\nGestor de Tareas Simple")
    print("1. Crear tarea")  # Opción para agregar una tarea
    print("2. Consultar tareas")  # Opción para mostrar todas las tareas
    print("3. Eliminar tarea")  # Opción para eliminar una tarea
    print("4. Salir")  # Opción para salir del programa
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Ingresa la tarea: ")
        agregar_tarea(tarea)  # Intenta agregar la tarea recibida
    elif opcion == "2":
        mostrar_tareas()  # Muestra todas las tareas actuales
    elif opcion == "3":
        mostrar_tareas()  # Muestra el listado primero para elegir
        try:
            num = int(input("Número de tarea a eliminar: "))
            eliminar_tarea(num)  # Elimina la tarea por número si es válido
        except ValueError:
            print("❌ Sólo se permite número.")  # Controla error por datos no numéricos
    elif opcion == "4":
        print("\n👋 ¡Hasta luego! Gracias por usar el gestor.")
        break  # Sale del programa
    else:
        print("\n🚫 Opción inválida. Intenta con las opciones disponibles.")  # Mensaje si la opción no existe
