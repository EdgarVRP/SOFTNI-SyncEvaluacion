class Cliente:
    def __init__(self , _id, id_cliente, nombre, ingreso_mensual, gastos_mensuales, puntuacion_credito, monto_solicitado, plazo_meses, tasa_interes, aprobado):
        self._id = _id
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.ingreso_mensual = ingreso_mensual
        self.gastos_mensuales = gastos_mensuales
        self.puntuacion_credito = puntuacion_credito
        self.monto_solicitado = monto_solicitado
        self.plazo_meses = plazo_meses
        self.tasa_interes = tasa_interes
        self.aprobado = aprobado
