# ------------------Factory--------------- #
# ¿Que es?
Defina el método utilizado para crear el objeto y no la llamada directa al constructor. Las subclases pueden anular este método para cambiar la clase de los objetos que crean.
# Para que sirve
•	Define una interfaz para crear objetos, pero permite que las subclases decidan qué clase instanciar. Los métodos de fábrica permiten que las clases descarguen la instanciación a las subclases.
•	Definición de un constructor "virtual".
•	El nuevo operador se considera malicioso.
# Dificultades
El marco debe estandarizar el modelo arquitectónico para diferentes aplicaciones, pero permitir que las aplicaciones individuales definan sus propios objetos de dominio y manejen la creación de instancias.
