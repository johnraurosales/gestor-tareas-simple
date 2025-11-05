tareas = []


def agregar_tarea(tarea):
    if tarea.strip() == "":
        print("❌ La tarea no puede estar vacía.")
    else:
        tareas.append(tarea)
        print("\n✅ ¡Tarea agregada exitosamente!")


def mostrar_tareas():
    if not tareas:
        print("\n📋 No hay tareas pendientes. ¡Agrega una nueva!")
    else:
        print("\n📝 Listado de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")


def eliminar_tarea(num):
    if 0 < num <= len(tareas):
        tarea = tareas.pop(num - 1)
        print(f"\n🗑️ Tarea '{tarea}' eliminada correctamente.")
    else:
        print("\n⚠️ Número de tarea inválido. Intenta otra vez.")


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
        try:
            num = int(input("Número de tarea a eliminar: "))
            eliminar_tarea(num)
        except ValueError:
            print("❌ Sólo se permite número.")
    elif opcion == "4":
        print("\n👋 ¡Hasta luego! Gracias por usar el gestor.")
        break
    else:
        print("\n🚫 Opción inválida. Intenta con las opciones disponibles.")
