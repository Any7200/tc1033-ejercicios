class Vehiculos:
    def __init__(self, _matricula, _medio, _capacidad, _velocidad_max):
        self.matricula = _matricula
        self.medio = _medio
        self.capacidad = _capacidad
        self.velocidad_max = _velocidad_max
class Terrestres(Vehiculos):
    def __init__(self,_n_ruedas,_datos_motor,_n_puertas):
        self.n_ruedas = _n_ruedas
        self.datos_motor = _datos_motor
        self.n_puertas = _n_puertas
    def comprobar_tipo(self):
        pass
class Maritimos(Vehiculos):
    def __init__(self,_tipo_propulsion):
        self.tipo_propulsion = _tipo_propulsion
class Aereos(Vehiculos):
    pass