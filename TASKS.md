# Tasks

Cada tarea ejecuta requisitos y criterios de `REQUIREMENTS.md` y `SPEC.md`; no añade reglas de producto.

## T-01 Project setup
- Goal: Crear paquete, configuración de pruebas, datos ficticios y documentación de arranque.
- Files: `pyproject.toml`, `README.md`, `src/customer_search/__init__.py`, `src/customer_search/data.py`.
- Acceptance: El proyecto puede instalarse localmente y contiene los datos de demostración de Q-01.
- Verification: Instalación editable y comprobación de importación.

## T-02 Domain model
- Goal: Definir el registro de cliente usado por FR-04.
- Files: `src/customer_search/models.py`, `src/customer_search/data.py`.
- Acceptance: Cada registro tiene `id`, `name` y `email`.
- Verification: Prueba de construcción y lectura de campos.

## T-03 Search logic
- Goal: Implementar FR-01 a FR-03 y las reglas de orden y no duplicación.
- Files: `src/customer_search/search.py`.
- Acceptance: Coincidencias parciales por nombre o correo sin distinción de mayúsculas.
- Verification: Pruebas de AC-01 a AC-03 y reglas de búsqueda.

## T-04 Validation and errors
- Goal: Implementar FR-05 y FR-06 y la interfaz CLI.
- Files: `src/customer_search/search.py`, `src/customer_search/cli.py`, `src/customer_search/__main__.py`.
- Acceptance: Mensajes y códigos de salida establecidos en `SPEC.md`.
- Verification: Pruebas de AC-04 a AC-06 y argumentos inválidos.

## T-05 Tests
- Goal: Completar las pruebas automatizadas y la cobertura de criterios de aceptación.
- Files: `tests/test_search.py`, `tests/test_cli.py`.
- Acceptance: AC-01 a AC-07 comprobados con pruebas de comportamiento.
- Verification: `pytest -v`.

## T-06 Documentation
- Goal: Registrar uso, trazabilidad, revisión y resultados finales.
- Files: `README.md`, `docs/traceability.md`, `results/agent-report.md`, `AI_USAGE_LOG.md`.
- Acceptance: AC-08 y AC-09 tienen evidencia; trazabilidad completa y registros consistentes.
- Verification: Revisión de documentos y ejecución documentada de la CLI y `pytest -v`.
