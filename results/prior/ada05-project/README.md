# Customer Search — ADA-05

CLI local para buscar clientes ficticios por nombre o correo electrónico. Acepta fragmentos, ignora mayúsculas y conserva el orden de los datos de entrada.

## Requisitos

- Python 3.11 o superior.
- `pytest` para ejecutar las pruebas.
- No se requieren credenciales, red, base de datos ni API de pago durante la ejecución.

## Instalación

Desde la raíz del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[test]'
```

La instalación incluye `pytest` como dependencia opcional de pruebas; la aplicación no tiene dependencias externas de ejecución.

## Ejecución

Con el entorno activado:

```bash
customer-search ana
customer-search example.com
```

También puede ejecutarse sin instalar el paquete:

```bash
PYTHONPATH=src python3 -m customer_search ana
```

El término se pasa como un único argumento. Si contiene espacios, usa comillas: `customer-search "ana lópez"`. Una búsqueda sin coincidencias muestra `No se encontraron clientes.`; un término vacío produce error y código de salida 2.

Los cuatro clientes del archivo `src/customer_search/data.py` son ficticios. No hay escritura de datos.

## Pruebas

```bash
pytest -v
```

## Documentación del ADA

- `REQUIREMENTS.md`: requisitos con IDs estables.
- `SPEC.md`: comportamiento y criterios de aceptación.
- `ARCHITECTURE.md`: componentes y decisiones técnicas.
- `TASKS.md`: secuencia de trabajo.
- `AGENTS.md`: instrucciones para el agente.
- `docs/traceability.md`: requisito → criterio → tarea → código → prueba.
- `AI_USAGE_LOG.md`: decisiones e interacciones relevantes de IA.
- `results/agent-report.md`: secuencia de trabajo, verificaciones y revisión personal.
- `docs/reflection.md`: reflexión sobre las decisiones y el proceso del proyecto.
