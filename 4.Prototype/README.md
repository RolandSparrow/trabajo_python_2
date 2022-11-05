# --------------Prototype------------- #
# ¿Que es?
Un patrón de diseño de compilación que tiene como objetivo reducir la cantidad de clases utilizadas en una aplicación. Puede copiar objetos existentes independientemente de la implementación concreta de la clase. En general, los objetos aquí se crean copiando la instancia del prototipo en tiempo de ejecución.
# Para que sirve
•	Utilice una instancia de prototipo para especificar el tipo de objeto que desea crear y, a continuación, copie este prototipo para crear un nuevo objeto. 
•	Adopte una instancia de la clase para utilizarla como criador para todas las instancias futuras.
•	El nuevo operador se considera malicioso.
# Dificultades
La aplicación "conecta" la clase de objeto para crear en cada expresión "nueva".
