Gestor de Tareas Simple
Este proyecto es un gestor de tareas interactivo hecho en Python para consola. Permite practicar los conceptos básicos
de programación, control de versiones (Git/GitHub) y documentación.

Funcionalidades
Agregar tarea: Añade una nueva tarea (evita tareas vacías).

Consultar tareas: Muestra todas las tareas pendientes, con numeración.

Eliminar tarea: Elimina la tarea seleccionada por número, con manejo de errores si la entrada es incorrecta.

Mensajes claros: Notificaciones visuales para cada acción.

Validaciones: Asegura que no se agreguen tareas vacías y que la opción de eliminación sólo acepte números válidos.

Uso
Ejecuta en consola:

bash
python gestor_tareas_simple.py
Menú principal:

1. Crear tarea: Ingresa el texto de la tarea para agregarla.

2. Consultar tareas: Muestra el listado numerado de tareas.

3. Eliminar tarea: Solicita el número de tarea para eliminarla.

4. Salir: Termina el programa.

Estructura del código
Cada función incluye un docstring que explica su objetivo y funcionamiento.

El menú principal controla la interacción y cada acción llamando a funciones separadas.

El código incluye comentarios aclarando cada bloque.