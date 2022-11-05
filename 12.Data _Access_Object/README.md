# --------------Data Access Object------------- #
# ¿Que es?
Casi todas las aplicaciones actuales necesitan acceso a al menos una fuente de datos. Estas fuentes suelen ser bases de datos relacionales, por lo que acceder a los datos no es un problema. La mayor parte del código debe ser refactorizado.
# Para que sirve
Sugiero separar completamente la lógica comercial de la lógica para acceder a los datos. De esta forma, las DAO proporcionan los métodos necesarios para insertar, actualizar, eliminar y recuperar información. La capa empresarial, por otro lado, solo considera la lógica empresarial y utiliza DAO para interactuar con las fuentes de datos.
# Dificultades
Al acceder a los datos, es importante que la implementación y el formato de la información puedan variar de una fuente de datos a otra. Implementación de la lógica de acceso a datos en la lógica empresarial Estos pueden diferir. Es necesario implementar una lógica diferente para acceder a diferentes fuentes de datos.
