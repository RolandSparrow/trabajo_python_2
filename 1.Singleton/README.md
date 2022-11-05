# ------------------Singleton--------------- #
# ¿Qué es?
El patrón singleton es un patrón de diseño de creación destinado a garantizar que una clase tenga solo una instancia y proporcione un único punto de acceso a esa instancia. Este patrón se usa normalmente (entre otras cosas) para registrar problemas cuando desea centralizar todo con una sola instancia del registrador.
# Para que sirve
•	Asegúrese de que solo haya una instancia de la clase y proporcione un punto de acceso global a esa instancia.
•	encapsuló "inicialización justo a tiempo" o "inicialización en el primer uso".
# Dificultades
•	Una aplicación debe tener solo una instancia del objeto. También requiere inicialización diferida y acceso global.