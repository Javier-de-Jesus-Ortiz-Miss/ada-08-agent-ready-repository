# Customer Search Feature

## Goal

Permitir localizar registros existentes de clientes mediante una CLI local con un solo término.

## Requirements Covered

- FR-01
- FR-02
- FR-03
- FR-04
- FR-05
- FR-06
- NFR-01
- NFR-02
- NFR-03

## Scope

Una ejecución recibe un término de búsqueda, consulta una lista fija de clientes ficticios en memoria y presenta las coincidencias.

## Out of Scope

Alta, edición o eliminación de clientes; persistencia; API HTTP; paginación; clasificación por relevancia; búsqueda por otros campos.

## Domain Model

`Customer` tiene `id` (texto no vacío), `name` (texto) y `email` (texto). El conjunto de demostración contiene registros ficticios. Los datos se tratan como solo lectura.

## Search Rules

- Se eliminan los espacios al inicio y final del término.
- Se compara el término normalizado con `name` y `email` usando `str.casefold()`.
- Una coincidencia es una subcadena en cualquiera de esos dos campos.
- Cada cliente aparece a lo sumo una vez aunque coincida en ambos campos.
- Se conserva el orden de entrada de los clientes.
- Los espacios interiores del término se conservan.

## Validation Rules

- El término debe ser una cadena de texto.
- Tras eliminar espacios exteriores, debe contener al menos un carácter.
- La CLI exige exactamente un argumento de búsqueda. La ausencia o exceso de argumentos produce un mensaje de uso.

## Error Handling

- Un término inválido en la función de búsqueda produce `ValueError` con un mensaje legible.
- En la CLI, un término vacío o de solo espacios produce un mensaje de error en `stderr` y código de salida 2.
- La ausencia o exceso de argumentos la gestiona `argparse`, con código 2.
- Una búsqueda válida sin coincidencias produce el mensaje `No se encontraron clientes.` y código 0.

## Acceptance Criteria

- **AC-01 (FR-01):** Un único término encuentra clientes cuyo nombre o correo contiene ese término.
- **AC-02 (FR-02):** Un fragmento que no sea el valor completo encuentra el cliente correspondiente.
- **AC-03 (FR-03):** Cambiar mayúsculas y minúsculas del término no cambia las coincidencias.
- **AC-04 (FR-04):** La salida muestra identificador, nombre y correo de cada coincidencia.
- **AC-05 (FR-05):** Sin coincidencias, la CLI muestra el mensaje definido y termina con código 0.
- **AC-06 (FR-06):** Un término vacío o de solo espacios se rechaza con un mensaje útil; la CLI termina con código 2.
- **AC-07 (NFR-01):** `pytest -v` ejecuta pruebas automatizadas para AC-01 a AC-06 y las reglas de orden y no duplicación.
- **AC-08 (NFR-02):** Una búsqueda funciona sin red ni credenciales y solo usa la biblioteca estándar de Python en tiempo de ejecución.
- **AC-09 (NFR-03):** `README.md` indica requisitos de Python, instalación, ejecución y pruebas.

## Test Scenarios

- Buscar un fragmento de nombre, un fragmento de correo y un término presente en ambos campos.
- Repetir una búsqueda con variantes de mayúsculas.
- Verificar orden y ausencia de duplicados.
- Buscar un término inexistente.
- Probar `""`, `"   "`, una entrada no textual en la función y argumentos faltantes o extra en la CLI.
- Verificar los campos impresos y los códigos de salida.

## Constraints

Se aplican C-01 a C-03 y A-01 a A-02 de `REQUIREMENTS.md`. No se necesita conexión ni API de pago.

## Open Questions

N/A: Q-01 y Q-02 quedaron resueltas en `REQUIREMENTS.md` para esta entrega.
