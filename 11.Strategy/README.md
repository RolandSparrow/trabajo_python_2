# --------------Strategy------------- #
# ¿Que es?
Una estrategia es un patrón de diseño de comportamiento que convierte un conjunto de comportamientos en un objeto y los hace intercambiables dentro del objeto de contexto original.
# Para que sirve
•	Definir una familia de algoritmos, encapsulando cada uno y haciéndolos intercambiables. Esta estrategia permite que el algoritmo cambie independientemente de los clientes que lo utilicen.
•	Capture la abstracción en las interfaces y oculte los detalles de implementación en las clases derivadas.
# Dificultades
Una de las estrategias dominantes en el diseño orientado a objetos es el "principio de abrir-cerrar".
El diagrama muestra cómo se logra esto de forma rutinaria: encapsulando los detalles de la interfaz en la clase base e incorporando los detalles de implementación en la clase derivada.
