menu = (
    "\n#### ¡Bienvenido al juego del millón copiado de Susana Gimenez! ####\n\n"
    "1. Inciar Juego\n"
    "2. Instrucciones\n"
    "3. Estadisticas\n"
    "4. Informacion de todos los usuarios\n"
    "5. Configuracion\n" \
    "6. Agregar nuevo usuario\n"
    "7. Guardar y Salir\n\n"
    "Ingrese una opción: "
)

instrucciones = (
    "\n### Instrucciones ###\n\n"
    "Al inicio del juego se le darán $1.000.000.\n"
    "Luego 8 preguntas de diferentes categorías, que usted eliga.\n"
    "Por cada pregunta tendrá 4 opciones en la cual usted\n"
    "tendra que decidir cuanto apostar en cada opción.\n"
    "De acuerdo al nivel de dificultad tendrá entre 10 a 30 segundos para decidir.\n"
    "Lo que haya apostado bien seguirá para la siguiente ronda\n"
    "Si no, pierde el dinero.\n\n"
    "¡Salve al Millón!\n"

    "Creado por Fransico Anabia y Brandon Castillo. 2025.\n"
)

mensaje_dificultad = (
    "\n### Seleccione la dificultad del juego ###\n\n"
    "1. Fácil\n"
    "2. Media\n"
    "3. Difícil\n"
    "4. Volver al menú panterior\n\n"
    "Ingrese una opción: "
)

mensaje_configuraciones = (
    "\n### Configuraciones ###\n\n"
    "1. Cambiar Dificultad\n"
    "2. Cambiar Categoría\n"
    "3. Ver Configuración Actual\n"
    "4. Volver al menú principal\n\n"
    "Ingrese una opción: "
)

mensaje_categoria = (
    "\n### Seleccione la categoría del juego ###\n\n"
    "1. Ciencia\n"
    "2. Arte\n"
    "3. Historia\n"
    "4. Matematicas\n"
    "5. Deportes\n"
    "6. Geografia\n"
    "7. Todas las categorías\n"
    "8. Volver al menú anterior\n\n"
    "Ingrese una opción: "
)

mensaje_usuarios_stats = (
    "\n### Estadísticas de Usuarios ###\n\n"
    "1. Ver TOP 10 usuarios\n"
    "2. Ver usuarios arriba del promedio\n"
    "3. Ver usuarios con más participaciones\n"
    "4. Volver al menú principal\n\n"
    "Ingrese una opción: "
)

mensajes_config = [mensaje_configuraciones, mensaje_dificultad, mensaje_categoria]

bienvenida_minijuego = ("\n### ¡Bienvenidos al minijuego! ###\n"
    "Este minijuego te dara una chance más para que puedas seguir jugando.\n"
    "Si ganas, regresas con el mismo dinero que tenías antes de perderlo.\n\n"
    "El juego consiste en adivinar una palabra de 5 caracteres,\n"
    "Vas a tener 6 intentos para adivinarla,\n"
    "por cada letra que coincida con la palabra, se pinta de verde,\n"
    "si la letra esta en la palabra pero no coincide en el orden, se muestra en amarillo.\n"
    "¿Estas listo? ¡Vamos!"
)