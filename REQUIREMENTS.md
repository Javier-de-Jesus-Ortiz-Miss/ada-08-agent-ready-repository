# Requirements — Customer Search

## Historia de usuario

Como usuario, quiero buscar clientes por nombre o correo electrónico para encontrar rápidamente el registro que necesito.

## Requisitos funcionales

- **FR-01 — Búsqueda unificada:** El usuario puede introducir un único término de búsqueda para consultar clientes por nombre o correo electrónico.
- **FR-02 — Coincidencia parcial:** Un cliente coincide cuando el término aparece como parte de su nombre o de su correo electrónico; no se exige una coincidencia exacta.
- **FR-03 — Independencia de mayúsculas:** La búsqueda produce los mismos resultados aunque cambien las mayúsculas o minúsculas del término o de los datos del cliente.
- **FR-04 — Resultados identificables:** Cada resultado muestra, como mínimo, el identificador, el nombre y el correo electrónico del cliente.
- **FR-05 — Sin coincidencias:** Cuando ningún cliente coincide, la aplicación informa que no se encontraron resultados, sin presentar registros ajenos a la búsqueda.
- **FR-06 — Validación del término:** La aplicación rechaza un término vacío o compuesto solo por espacios e informa al usuario cómo corregirlo.

## Requisitos no funcionales

- **NFR-01 — Pruebas automatizadas:** El comportamiento de búsqueda y validación debe poder verificarse con pruebas ejecutables mediante `pytest`.
- **NFR-02 — Ejecución local:** La función debe ejecutarse localmente sin servicios externos ni API de pago.
- **NFR-03 — Entorno reproducible:** El proyecto debe documentar cómo instalar sus dependencias y ejecutar la aplicación y sus pruebas con Python 3.11 o superior.

## Preguntas abiertas

- **Q-01 — Datos de ejemplo (resuelta):** Se usará un conjunto pequeño de clientes ficticios incluido en el proyecto.
- **Q-02 — Orden de resultados (resuelta):** Se conservará el orden de los datos de entrada.

## Restricciones y supuestos

- **C-01:** El proyecto se construye desde cero y usa herramientas gratuitas.
- **C-02:** La implementación por agente debe realizarse con Antigravity CLI (`agy`), con revisión y validación del código por el estudiante.
- **C-03:** Se mantiene un registro de uso de IA durante las etapas que influyan en el producto.
- **A-01:** La primera versión será una CLI de Python con datos en memoria; no requiere base de datos ni API HTTP.
- **A-02:** Los registros de clientes ya existen al ejecutar la búsqueda. Crear, editar o eliminar clientes queda fuera de esta feature.

## Decisiones de alcance

El proyecto usa una CLI y clientes ficticios en memoria porque el objetivo es demostrar la búsqueda y sus pruebas. Se conserva el orden de entrada para evitar añadir una regla de clasificación que no necesita esta versión. Estas decisiones corresponden a Q-01, Q-02 y A-01.

## Revisión del documento

Yo conservé la trazabilidad de los requisitos y las decisiones de alcance en la documentación técnica.
