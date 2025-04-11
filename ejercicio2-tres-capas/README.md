# Ejercicio 2 - Arquitectura en Tres Capas

Este ejercicio implementa una aplicación Flask utilizando la arquitectura de **tres capas**:

## Capas:

- **Capa de Presentación** (`app.py`) – Define las rutas HTTP.
- **Capa de Lógica de Negocio** (`logic.py`) – Procesa datos, reglas de negocio.
- **Capa de Acceso a Datos** (`data.py`) – Almacena productos en memoria.

## Funcionalidades:

- Agregar productos (`POST /productos`)
- Listar productos (`GET /productos`)

## Ventajas frente al modelo monolítico:

- Código más limpio y mantenible.
- Mayor reutilización de lógica.
- Permite pruebas unitarias más fácilmente.
- Escalable a otras interfaces o tecnologías.
