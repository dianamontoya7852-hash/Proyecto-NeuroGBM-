"""
Proyecto: NeuroGBM
Archivo: main.py

Archivo principal de ejecución.
Importa las clases desde modelos.py y realiza
las pruebas de funcionamiento del sistema.
"""

# ==========================================
# IMPORTACIÓN DE CLASES
# ==========================================

from modelos import (
    Usuario,
    Paciente,
    Medico,
    Administrador,
    Sintoma,
    Tratamiento,
    Cita
)


# ==========================================
# INSTANCIACIÓN DE OBJETOS
# ==========================================

print("======================================")
print("       SISTEMA NEUROGBM")
print("======================================")

# Creación de paciente
paciente = Paciente(
    1,
    "Ana López",
    "ana@example.com",
    "clave123",
    "Paciente",
    45,
    "Glioblastoma"
)

# Creación de médico
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

# Creación de administrador
administrador = Administrador(
    3,
    "Laura Gómez",
    "laura@example.com",
    "admin123",
    "Administrador"
)


# ==========================================
# PRUEBA DE COMPOSICIÓN
# ==========================================

print("\n--- PRUEBA DE COMPOSICIÓN ---")

sintoma = Sintoma(
    1,
    "Dolor de cabeza",
    "Dolor persistente",
    7,
    "2026-11-09"
)

tratamiento = Tratamiento(
    1,
    "Farmacológico",
    "Tratamiento de ejemplo",
    "Según indicación médica",
    "Según prescripción",
    "2026-11-09",
    "Por determinar"
)

# El paciente contiene objetos Sintoma y Tratamiento
paciente.registrar_sintoma(sintoma)
paciente.recibir_tratamiento(tratamiento)

# Consulta de objetos contenidos
print("\nSíntomas del paciente:")

for sintoma_registrado in paciente.consultar_sintomas():
    print(
        f"- {sintoma_registrado.tipo}: "
        f"Intensidad {sintoma_registrado.intensidad}/10"
    )

print("\nTratamientos del paciente:")

for tratamiento_registrado in paciente.consultar_tratamientos():
    print(f"- {tratamiento_registrado.nombre}")


# ==========================================
# PRUEBA DE HERENCIA
# ==========================================

print("\n--- PRUEBA DE HERENCIA ---")

paciente.iniciar_sesion()
medico.iniciar_sesion()
administrador.iniciar_sesion()


# ==========================================
# PRUEBA DE ENCAPSULAMIENTO
# ==========================================

print("\n--- PRUEBA DE ENCAPSULAMIENTO ---")

print(
    "Contraseña correcta:",
    paciente.verificar_contrasena("clave123")
)

print(
    "Contraseña incorrecta:",
    paciente.verificar_contrasena("incorrecta")
)


# ==========================================
# PRUEBA DE POLIMORFISMO
# ==========================================

print("\n--- PRUEBA DE POLIMORFISMO ---")

usuarios = [paciente, medico, administrador]

for usuario in usuarios:
    usuario.mostrar_informacion()
    print("------------------------------")


# ==========================================
# PRUEBA DE INTERACCIÓN ENTRE CLASES
# ==========================================

print("\n--- PRUEBA DE INTERACCIÓN ---")

cita = Cita(
    1,
    "2026-11-15",
    "Seguimiento oncológico",
    paciente,
    medico
)

medico.consultar_paciente(paciente)
medico.registrar_cita(cita)
cita.mostrar_detalles()


print("\n======================================")
print("  PRUEBAS DEL SISTEMA NEUROGBM FINALIZADAS")
print("======================================")
