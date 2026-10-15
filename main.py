"""
Proyecto: NeuroGBM
Descripción:
Sistema básico para organizar el seguimiento de pacientes con glioblastoma.
Permite registrar pacientes, síntomas, tratamientos y consultas médicas.
El proyecto aplica programación orientada a objetos mediante clases,
encapsulamiento, herencia, super() y polimorfismo.
"""


# Creación de la clase base
class Usuario:
    def __init__(self, id_usuario, nombre, correo, contrasena, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.correo = correo
        self.__contrasena = contrasena
        self.rol = rol

    # Aplicación de encapsulamiento
    def verificar_contrasena(self, contrasena):
        return self.__contrasena == contrasena

    def iniciar_sesion(self):
        print(f"{self.nombre} ha iniciado sesión.")

    def cerrar_sesion(self):
        print(f"{self.nombre} ha cerrado sesión.")

    def editar_perfil(self, nuevo_correo):
        self.correo = nuevo_correo
        print("Perfil actualizado correctamente.")


# Creación de la clase Paciente
class Paciente(Usuario):
    def __init__(
        self, id_usuario, nombre, correo, contrasena,
        rol, edad, diagnostico
    ):
        # Uso de super() y herencia
        super().__init__(
            id_usuario, nombre, correo, contrasena, rol
        )
        self.edad = edad
        self.diagnostico = diagnostico
        self.__sintomas = []
        self.__tratamientos = []

    def registrar_sintoma(self, sintoma):
        self.__sintomas.append(sintoma)
        print("Síntoma registrado correctamente.")

    def consultar_sintomas(self):
        return self.__sintomas.copy()

    def recibir_tratamiento(self, tratamiento):
        self.__tratamientos.append(tratamiento)
        print("Tratamiento registrado correctamente.")

    def consultar_tratamientos(self):
        return self.__tratamientos.copy()

    # Sobrescritura de métodos (polimorfismo)
    def mostrar_informacion(self):
        print(f"Paciente: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Diagnóstico: {self.diagnostico}")


# Creación de la clase Sintoma
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


# Creación de la clase Tratamiento
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


# Creación de la clase Medico
class Medico(Usuario):
    def __init__(
        self, id_usuario, nombre, correo, contrasena,
        rol, especialidad, institucion, telefono
    ):
        # Uso de super() y herencia
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


# Creación de la clase Cita
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


# Sobrescritura de métodos (polimorfismo)
class Administrador(Usuario):
    def __init__(
        self, id_usuario, nombre, correo, contrasena, rol
    ):
        super().__init__(
            id_usuario, nombre, correo, contrasena, rol
        )

    def mostrar_informacion(self):
        print(f"Administrador del sistema: {self.nombre}")


# Función para demostrar el polimorfismo
def mostrar_usuario(usuario):
    if isinstance(usuario, Paciente):
        usuario.mostrar_informacion()
    elif isinstance(usuario, Administrador):
        usuario.mostrar_informacion()
    else:
        print(f"Usuario del sistema: {usuario.nombre}")


# Instanciación y pruebas
if __name__ == "__main__":
    paciente = Paciente(
        1,
        "Ana López",
        "ana@example.com",
        "clave123",
        "Paciente",
        45,
        "Glioblastoma"
    )

    medico = Medico(
        2,
        "Dr. Carlos Ruiz",
        "carlos@example.com",
        "medico123",
        "Médico",
        "Neurooncología",
        "Hospital General",
        "5551234567"
    )

    administrador = Administrador(
        3,
        "Laura Gómez",
        "laura@example.com",
        "admin123",
        "Administrador"
    )

    sintoma = Sintoma(
        1,
        "Dolor de cabeza",
        "Dolor persistente",
        7,
        "2026-10-15"
    )

    tratamiento = Tratamiento(
        1,
        "Farmacológico",
        "Tratamiento de ejemplo",
        "Según indicación médica",
        "Según prescripción",
        "2026-10-15",
        "Por determinar"
    )

    cita = Cita(
        1,
        "2026-10-20",
        "Seguimiento",
        paciente,
        medico
    )

    paciente.registrar_sintoma(sintoma)
    paciente.recibir_tratamiento(tratamiento)
    medico.consultar_paciente(paciente)
    medico.registrar_cita(cita)
    cita.mostrar_detalles()

    print("\n--- Prueba de encapsulamiento ---")
    print(
        "Contraseña correcta:",
        paciente.verificar_contrasena("clave123")
    )

    print("\n--- Prueba de polimorfismo ---")
    mostrar_usuario(paciente)
    mostrar_usuario(administrador)
    mostrar_usuario(medico)
