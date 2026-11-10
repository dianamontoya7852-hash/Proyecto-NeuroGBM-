# Proyecto NeuroGBM

**Sistema de seguimiento de pacientes con glioblastoma desarrollado en Python mediante programación orientada a objetos.**

## Descripción del proyecto

NeuroGBM es un sistema básico diseñado para organizar la información y el seguimiento de pacientes diagnosticados con glioblastoma. Permite gestionar usuarios, pacientes, médicos, síntomas, tratamientos y citas médicas.

El proyecto se desarrolla utilizando Python y aplica los principios fundamentales de la programación orientada a objetos.

## Objetivo

Desarrollar un sistema modular que permita representar las diferentes entidades relacionadas con el seguimiento de pacientes con glioblastoma, facilitando la organización de su información mediante clases y objetos.

## Estructura del proyecto

El proyecto está organizado en los siguientes archivos:

- **modelos.py:** contiene las definiciones de las clases Usuario, Paciente, Medico, Administrador, Sintoma, Tratamiento y Cita.
- **main.py:** contiene las importaciones, la instanciación de objetos y las pruebas de funcionamiento del sistema.
- **DIAGRAMA UML - AVANCE 3.pdf:** representa gráficamente las clases y sus relaciones.

## Principios de programación orientada a objetos

### 1. Herencia
Se utiliza una clase base llamada Usuario, de la cual heredan las clases Paciente, Medico y Administrador.

### 2. Encapsulamiento
Se protegen atributos mediante el uso de atributos privados, como la contraseña, los síntomas y los tratamientos.

### 3. Polimorfismo
Las clases Paciente, Medico y Administrador implementan su propia versión del método mostrar_informacion(), permitiendo diferentes comportamientos mediante una misma interfaz.

### 4. Composición
La clase Paciente contiene colecciones de objetos Sintoma y Tratamiento. Además, utiliza los métodos de estas clases para registrar sus respectivos elementos.

### 5. Modularización
El código se divide en dos módulos principales: modelos.py, que contiene las clases, y main.py, que importa dichas clases y ejecuta las pruebas del sistema.

## Pruebas de funcionamiento

Se realizaron pruebas para verificar:

- La creación e interacción de objetos.
- El funcionamiento de la herencia.
- La protección de atributos mediante encapsulamiento.
- El comportamiento polimórfico de las clases.
- La composición entre Paciente, Sintoma y Tratamiento.
- La correcta importación de clases desde modelos.py.

La ejecución del programa se verificó utilizando Google Colab, sin errores.

## Requisitos

- Python 3.
- Google Colab o cualquier entorno compatible con Python.

## Instrucciones de ejecución

1. Clonar el repositorio:

   `git clone https://github.com/dianamontoya7852-hash/Proyecto-NeuroGBM-.git`

2. Entrar a la carpeta del proyecto:

   `cd Proyecto-NeuroGBM-`

3. Ejecutar el archivo principal:

   `python main.py`

## Autor

Diana Montoya

**Proyecto académico — Programación**
