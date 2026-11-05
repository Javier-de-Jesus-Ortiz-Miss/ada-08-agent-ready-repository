# Skill Comparison - ADA-07

Mismo repositorio, base 8ab0a4f5f34804a2dc24c4b87a1aa5a2efdaabb5 y head 0bfa0b8836589366b0dd6fb6ceada326d7fa5a87. Un solo agente/sesión; revisiones secuenciales, no ensayo ciego. La segunda revisión puede beneficiarse del contexto previo; no se atribuye causalidad exclusiva a la Skill.

| Dimensión | reviewing-pull-requests 1.0.1 | code-review-and-quality, commit 1401c8b | Conclusión con evidencia |
|---|---|---|---|
| Trigger / routing | PR/rama/diff, readiness; excluye implementar/merge solo/Git genérico. | Review de cualquier autor y cambios antes de merge, incluso inline. | Propia más precisa para tarea del ADA; 9 casos asistidos. |
| Scope / boundaries | Draft-Only y no escritura remota explícitos. | Estándar de salud de código con verdict; no API read-only impuesta por texto. | Se mantiene límite del usuario y curso en ambas; cero escrituras remotas. |
| Workflow depth | Mapa AC, diff, tests, severity, reporte y script. | Tests primero, cinco ejes, mutación y verificación de build. | La segunda añade evidencia que un PASS de pytest no ofrecía. |
| Correctness | AC-01 a AC-09; 25 passed. | Misma suite y 4 mutaciones detectadas. | Ambas encuentran implementación conforme; la profesional prueba sensibilidad. |
| Architecture | CLI/domino/datos y modelo frozen revisados. | Invariante frozen retirado, suite sigue verde. | PF-01 identifica mejora concreta de cobertura, no defecto actual. |
| Security | secretos/validación/permisos pertinentes. | Checklist ampliado de límites y dependencias. | Datos locales ficticios; auth HTTP/XSS fuera de alcance, sin findings artificiales. |
| Performance | No eje detallado en v1. | Recorrido, recursos y adecuación al volumen explícitos. | No N+1: no DB. No benchmark para afirmar latencias o escalabilidad. |
| Tests / verification | pytest y reporte validado. | pytest, mutaciones, wheel y entrypoint instalado. | Más evidencia ejecutable: logs build.txt e installed-cli.txt, exit 0. |
| Severity model | MUST FIX / SHOULD FIX / OPTIONAL, IDs RF. | Critical / Required / Optional / Nit / FYI. | 0 blockers; propia 1 OPTIONAL, profesional 2 Optional. Ninguna fuerza findings. |
| Human review | YES obligatorio por validador. | Consejo/verdict sometido al humano por contexto. | Ambas conservan la decisión final del estudiante; su aceptación de los reportes todavía no está documentada. |
| References / composition | Checklist y severidad pequeños; script y asset. | Dos checklists repo-wide y Skills especializadas sugeridas. | Instalación completa preserva ../../references; no composición innecesaria. |
| Reusability | Paths relativos, base/head parametrizados, sin PR fijo. | Revisión general de distintos stacks, heurísticas extensas. | Ambas reutilizables en diseño; solo una fixture ejecutada, sin prueba multi-repo. |

## Qué aporta la profesional
Prueba experimental de la calidad de tests y verificación de empaquetado/entrada instalable. PF-01 se basa en un mutante que sobrevive, no en sospecha de lectura.

## Qué conservar de la propia
Trazabilidad por AC, salida Draft-Only, tres categorías del curso, contador verificable, evidencia por finding, stop por conflicto normativo, negativa explícita a merge y formato determinista. Facilitan evaluación académica y control de autoridad.

## Dos ejemplos de acciones concretas
1. RF-01/PF-02: añadir pruebas de lista y generador vacíos; entrada y resultado esperado [] expresos. Ambas revisiones son accionables.
2. PF-01: añadir test de FrozenInstanceError al intentar modificar el modelo. La revisión profesional aporta mejor respaldo experimental: quitar frozen deja 25/25 verdes.
Para este cambio, la profesional produjo evidencia más amplia y una sugerencia adicional; la propia produjo un reporte más fácilmente validable. Esto no demuestra superioridad general de una Skill ni de otro modelo.

## Hallazgos únicos
Profesional: PF-01, regresión de inmutabilidad sin test. Segundo finding profesional exclusivo: ninguno; no se inventa para llenar una lista.
Propia: ninguno exclusivo; RF-01 coincide con PF-02. Su aportación exclusiva es el contrato determinista del reporte, no un defecto nuevo. La pregunta del id no vacío es compartida y permanece abierta.

## Propuesta v2 y evaluación
Añadir performance por alcance; mutación opt-in en copia aislada; gates de build donde haya sistema de build; trazabilidad del commit/evidencia; distinguir read-only del código frente a generación local de reportes. Mantener SKILL.md breve mediante referencias condicionales.
Evaluar v2 en tres fixtures: CLI actual, defecto real de validación y proyecto sin build disponible. Exigir finding frozen en el mutante, cero falsa exigencia de npm/HTTP en CLI, no modificación fuente, reporte válido y mismos negativos sin activación. Comparar coste de contexto en palabras y tokenizer elegido, además de aciertos, falsos positivos y acciones fuera de scope.
No se implementa v2 aquí: es propuesta, no resultado observado.

## Qué NO copiar
No adoptar umbrales de líneas como bloqueos rígidos; no exigir auth/paginación a la CLI; no ejecutar mutación en fuente original; no convertir verdict Approve en permiso de GitHub; no instalar hooks ni meta-router como efecto implícito. Las políticas deben servir a los requisitos y a la autoridad autorizada.
