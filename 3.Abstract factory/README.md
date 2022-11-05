# --------------Abstract factory------------- #
# ¿Que es?
Los métodos de fábrica abstractos son un patrón de diseño creativo que le permite crear una familia de objetos relacionados sin especificar una clase concreta. El uso de métodos de fábrica abstractos proporciona la forma más fácil de producir muchos objetos de tipo similar. 
Proporciona una forma de encapsular grupos de fábricas individuales.
# Para que sirve
•	Proporciona una interfaz para crear una familia de objetos relacionados o dependientes sin especificar una clase concreta.
•	Jerarquía que incluye: construir muchas 'plataformas' y conjuntos de 'productos' posibles.
•	El nuevo operador se considera malicioso.
# Dificultades
Las dependencias de la plataforma se deben encapsular si se desea que la aplicación sea portátil. Estas "plataformas" pueden incluir sistemas de ventanas, sistemas operativos, bases de datos y más. Muy a menudo, esta encapsulación no está prediseñada y muchas declaraciones de casos #ifdef con opciones para todas las plataformas admitidas actualmente comienzan a proliferar como conejos en su código.
