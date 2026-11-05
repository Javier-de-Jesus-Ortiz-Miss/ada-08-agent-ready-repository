# AI Usage Log — ADA-05

Yo utilicé asistencia de IA durante el análisis, la documentación, la implementación y la validación. Yo organicé el registro por etapas técnicas del proyecto.

## Entrada 01 — Análisis del ADA

- **Objetivo técnico:** Analizar el enunciado e identificar los entregables antes de crear archivos.
- **Apoyo de la IA:** Leyó el enunciado, resumió las fases y revisó el estado de la carpeta del proyecto.
- **Mi participación:** Yo organicé el alcance y la secuencia de trabajo a partir del enunciado.
- **Resultado:** Se identificaron la búsqueda de clientes, los documentos requeridos, las pruebas y el registro de uso de IA. En este paso no se modificaron archivos.

## Entrada 02 — Requisitos (fase 1)

- **Objetivo técnico:** Preparar una propuesta de requisitos para la búsqueda de clientes.
- **Propuesta de la IA:** Redactar la historia de usuario, seis requisitos funcionales, tres no funcionales, restricciones, supuestos y dos preguntas abiertas. Se propuso una CLI local con datos en memoria como alcance inicial.
- **Mi revisión y decisión:** Leí y revisé la lista propuesta de requisitos funcionales y no funcionales. Aprobé su contenido y el alcance de CLI local con datos ficticios en memoria. 
- **Cambio en el producto:** Se creó `REQUIREMENTS.md`; Q-01, Q-02 y A-01 quedaron definidos para esta entrega.
- **Resultado:** El alcance quedó limitado a búsqueda local, sin administración de clientes ni persistencia.

## Entrada 03 — Especificación y planificación (fases 2 a 6)

- **Objetivo técnico:** Desarrollar la especificación, la arquitectura, las tareas y las instrucciones del agente a partir de los requisitos.
- **Etapa técnica:** La IA convirtió los requisitos ya definidos en criterios de aceptación, reglas de búsqueda, arquitectura y seis tareas verificables.
- **Propuesta de la IA:** Usar una función pura con clientes inyectados, `casefold()` para comparar y una CLI que traduzca los errores a códigos de salida.
- **Mi revisión y decisión:** Leí y aprobé los documentos de especificación, arquitectura y planificación. Acepté las propuestas técnicas de la IA para este alcance.
- **Cambio en el producto:** Se añadieron `SPEC.md`, `ARCHITECTURE.md`, `TASKS.md`, `AGENTS.md`, `README.md` y la estructura inicial, antes de implementar la feature.
- **Resultado:** Los requisitos conservaron sus IDs y la especificación los relacionó con criterios de aceptación.

## Entrada 04 — Implementación (T-01 a T-04)

- **Etapa técnica:** Se pidió a Antigravity CLI (`agy`) realizar T-01 después del commit base. Los primeros intentos fallaron por permisos y el intento en sandbox agotó el tiempo de espera. Un borrador tardío de `README.md` apareció en el árbol, sin reporte completo. Codex continuó T-01 y realizó T-02 a T-04.
- **Propuesta de la IA:** Paquete Python instalable, datos ficticios, modelo inmutable, búsqueda pura y CLI con `argparse`.
- **Mi revisión y decisión:** Leí y aprobé la implementación presentada. El código fue escrito por Codex, que continuó el trabajo después de los problemas de ejecución de `agy`.
- **Cambio en el producto:** Se añadieron `pyproject.toml` y `src/customer_search/`; se corrigió el README para que sus comandos coincidan con el paquete final.
- **Resultado:** La función de búsqueda quedó separada de la lectura de argumentos y de la presentación de resultados.

## Entrada 05 — Pruebas y revisión (T-05 y T-06)

- **Etapa técnica:** Codex comparó las reglas de `SPEC.md` con la implementación y preparó pruebas para búsqueda, validación y CLI.
- **Propuesta de la IA:** Pruebas de fragmentos, mayúsculas, orden, ausencia de duplicados, mensajes y códigos de salida; tabla de trazabilidad por requisito.
- **Mi revisión y decisión:** Leí y aprobé las pruebas, los resultados presentados y la documentación de trazabilidad. Codex diseñó y ejecutó las verificaciones registradas.
- **Cambio en el producto:** Se añadieron `tests/`, `docs/traceability.md`, `results/agent-report.md`, `docs/reflection.md` y documentación final. `pytest -v` aprobó 15 pruebas en la primera ejecución completa.
- **Resultado:** Las pruebas cubren búsqueda, validación y salida de la CLI; la trazabilidad conecta esas verificaciones con los requisitos.

## Entrada 06 — Documentación técnica

- **Objetivo técnico:** Preparar una explicación de la colaboración y de la revisión por fases.
- **Mi participación:** Aporté ideas y ajustes sobre cómo describir el trabajo y mi participación. Pedí apoyo para expresarlos con mayor claridad y revisé la versión resultante.
- **Aporte de la IA:** Codex resumió las interacciones y actualizó la documentación para distinguir mi revisión y aprobación de las propuestas y la implementación realizadas con IA.
- **Cambio en el producto:** Se ajustaron los textos de requisitos, reflexión, README, informe y este registro.
- **Resultado:** La documentación conserva las herramientas utilizadas, los cambios observados y los resultados de las pruebas.

## Alcance de las verificaciones

Codex ejecutó las pruebas y las verificaciones técnicas. Mi lectura y aprobación del trabajo quedaron confirmadas al cierre y están organizadas por fase en `results/agent-report.md`.
