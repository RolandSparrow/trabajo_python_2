# --------------Proxy------------- #
# ¿Que es?
El proxy es un patrón de diseño estructural que proporciona un objeto que actúa como sustituto de un objeto de servicio real utilizado por un cliente. Un proxy recibe las peticiones del cliente, realiza algún trabajo (control de acceso, almacenamiento en caché, etc.) y luego pasa la petición a un objeto de servicio.
# Para que sirve
•	Proporciona un sustituto o marcador de posición para otro objeto para controlar el acceso a ese objeto.
•	Utilice una capa adicional de direccionamiento indirecto para admitir el acceso distribuido, controlado o inteligente.
•	Agregue envolturas y delegaciones para proteger el componente real de complicaciones excesivas.
# Dificultades
Necesitas soportar objetos que requieran muchos recursos, y no quieres instanciar dichos objetos a menos que sean solicitados por el cliente.
