"""
Proyecto: NeuroGBM
Archivo: modelos.py

Contiene las clases del sistema de seguimiento
de pacientes con glioblastoma.

Se implementan:
- Herencia
- Encapsulamiento
- Polimorfismo
- Composición
"""


# ==========================================
# CLASE BASE: USUARIO
# ==========================================

class Usuario:
    def __init__(self, id_usuario, nombre, correo, contrasena, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.__contrasena = contrasena
        self.rol = rol

    # Encapsulamiento
    def verificar_contrasena(self, contrasena):
        return self.__contrasena == contrasena

    def iniciar_sesion(self):
        print(f"{self.nombre} ha iniciado sesión.")

    def cerrar_sesion(self):
        print(f"{self.nombre} ha cerrado sesión.")

    def editar_perfil(self, nuevo_correo):
        self.correo = nuevo_correo
        print("Perfil actualizado correctamente.")


# ==========================================
# CLASE PACIENTE: HERENCIA Y COMPOSICIÓN
# ==========================================

class Paciente(Usuario):
    def __init__(
        self, id_usuario, nombre, correo, contrasena,
        rol, edad, diagnostico
    ):
        super().__init__(
            id_usuario, nombre, correo, contrasena, rol
        )

        self.edad = edad
        self.diagnostico = diagnostico

        # Encapsulamiento y composición
        self.__sintomas = []
        self.__tratamientos = []

    def registrar_sintoma(self, sintoma):
        # Delegación: utiliza un método del objeto Sintoma
        sintoma.registrar_sintoma()

        # El paciente almacena el objeto Sintoma
        self.__sintomas.append(sintoma)

        print("Síntoma registrado correctamente.")

    def consultar_sintomas(self):
        return self.__sintomas.copy()

    def recibir_tratamiento(self, tratamiento):
        # Delegación: utiliza un método del objeto Tratamiento
        tratamiento.registrar_tratamiento()

        # El paciente almacena el objeto Tratamiento
        self.__tratamientos.append(tratamiento)

        print("Tratamiento registrado correctamente.")

    def consultar_tratamientos(self):
        return self.__tratamientos.copy()

    # Polimorfismo: sobrescritura de método
    def mostrar_informacion(self):
        print(f"Paciente: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Diagnóstico: {self.diagnostico}")


# ==========================================
# CLASE AUXILIAR: SINTOMA
# ==========================================

class Sintoma:
    def __init__(
        self, id_sintoma, tipo, descripcion,
        intensidad, fecha_registro
    ):
        self.id_sintoma = id_sintoma
        self.tipo = tipo
        self.descripcion = descripcion
        self.intensidad = intensidad
        self.fecha_registro = fecha_registro

    def registrar_sintoma(self):
        print(f"Registrando síntoma: {self.tipo}")

    def editar_sintoma(self, nueva_descripcion):
        self.descripcion = nueva_descripcion
        print("Descripción del síntoma actualizada.")

    def eliminar_sintoma(self):
        print(f"Solicitud de eliminación del síntoma {self.id_sintoma}.")


# ==========================================
# CLASE: TRATAMIENTO
# ==========================================

class Tratamiento:
    def __init__(
        self, id_tratamiento, tipo, nombre, dosis,
        frecuencia, fecha_inicio, fecha_fin, observaciones=""
    ):
        self.id_tratamiento = id_tratamiento
        self.tipo = tipo
        self.nombre = nombre
        self.dosis = dosis
        self.frecuencia = frecuencia
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.observaciones = observaciones

    def registrar_tratamiento(self):
        print(f"Tratamiento registrado: {self.nombre}")

    def editar_tratamiento(self, nueva_dosis):
        self.dosis = nueva_dosis
        print("Dosis actualizada.")

    def finalizar_tratamiento(self):
        print(f"Tratamiento finalizado: {self.nombre}")


# ==========================================
# CLASE MEDICO: HERENCIA
# ==========================================

class Medico(Usuario):
    def __init__(
        self, id_usuario, nombre, correo, contrasena,
        rol, especialidad, institucion, telefono
    ):
        super().__init__(
            id_usuario, nombre, correo, contrasena, rol
        )

        self.especialidad = especialidad
        self.institucion = institucion
        self.telefono = telefono

    def consultar_paciente(self, paciente):
        print(f"Consultando expediente de {paciente.nombre}.")

    def registrar_cita(self, cita):
        print(f"Cita registrada para {cita.paciente.nombre}.")

    def actualizar_tratamiento(self, tratamiento, nueva_dosis):
        tratamiento.editar_tratamiento(nueva_dosis)

    def revisar_estudios(self):
        print("Revisando estudios médicos.")


# ==========================================
# CLASE: CITA
# ==========================================

class Cita:
    def __init__(self, id_cita, fecha, motivo, paciente, medico):
        self.id_cita = id_cita
        self.fecha = fecha
        self.motivo = motivo
        self.paciente = paciente
        self.medico = medico

    def mostrar_detalles(self):
        print(f"Cita: {self.fecha}")
        print(f"Motivo: {self.motivo}")
        print(f"Paciente: {self.paciente.nombre}")
        print(f"Médico: {self.medico.nombre}")


# ==========================================
# CLASE ADMINISTRADOR: HERENCIA
# ==========================================

class Administrador(Usuario):
    def __init__(
        self, id_usuario, nombre, correo, contrasena, rol
    ):
        super().__init__(
            id_usuario, nombre, correo, contrasena, rol
        )

    # Polimorfismo: sobrescritura de método
    def mostrar_informacion(self):
        print(f"Administrador del sistema: {self.nombre}")
