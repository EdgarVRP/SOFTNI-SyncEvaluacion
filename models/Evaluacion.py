class Cliente:
    def __init__(self , _id, idPrestatario, nombre, ingreso_mensual,puntuacion_credito, creditoAceptado):
        self._id = _id
        self.idPrestatario = idPrestatario
        self.nombre = nombre
        self.ingreso_mensual = ingreso_mensual
        self.puntuacion_credito = puntuacion_credito
        self.creditoAceptado = creditoAceptado
