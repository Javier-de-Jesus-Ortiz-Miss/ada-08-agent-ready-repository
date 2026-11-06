# Mi análisis de impacto de repository readiness

## Mi criterio de evaluación

Yo evalué ocho dimensiones con los pesos de ADA-08 y preservé la auditoría inicial antes de modificar la preparación del repositorio. Yo separé el funcionamiento de la aplicación, la preparación del repositorio y la validez experimental. Yo no interpreté una diferencia de puntuación como una demostración estadística de mejor desempeño del modelo.

## Mis mejoras y la fricción que atendí

| ID | Categoría | Problema que yo observé | Cambio que yo implementé | Evidencia que yo conservé |
|---|---|---|---|---|
| I-01 | Context | Yo encontré instrucciones parciales sin contrato completo de operación. | Yo concentré fuentes, comandos, límites, stop conditions y DoD en AGENTS. | Yo validé encabezados, fuentes y secciones con el checker. |
| I-02 | Navigation | Yo tuve que relacionar manualmente el modelo, SPEC y pruebas. | Yo creé REPO_MAP con rutas por pregunta y guía de cambios. | Yo comprobé enlaces locales y referencias. |
| I-03 | Executable Knowledge | Yo solo tenía pytest como validación documentada. | Yo añadí verify_repo con pytest, Ruff y contrato, sin descargas durante el gate. | Yo conservé el log del gate completo. |
| I-04 | Guardrail | Yo no tenía detección de cambios en evidencia o datos protegidos. | Yo añadí hashes y cobertura exacta del manifiesto. | Yo ejecuté mutaciones de datos y eliminación de una entrada del manifiesto. |
| I-05 | Guardrail | Yo tenía arquitectura explícita sin un check de imports. | Yo comprobé dependencias directas y llamadas de I/O en dominio. | Yo probé imports indebidos y open sin ejecutar código mutado. |
| I-06 | Test | Yo detecté un constructor que incumplía un invariante existente. | Yo implementé la misma tarea de producto con diez casos en cada corrida. | Yo conservé seis fallos esperados antes y la suite verde después. |
| I-07 | CI Check | Yo no tenía validación fuera de la sesión local. | Yo configuré Actions para invocar el mismo gate con permisos de lectura. | Yo validé la estructura y paridad local; yo no afirmé una ejecución remota. |
| I-08 | Human Gate | Yo podía confundir evidencia generada con revisión humana. | Yo documenté decisiones que requieren intervención y el límite de la sesión compartida. | Yo marqué el protocolo estricto PARTIAL y conservé la autoría de la automatización. |

## Lo que yo puedo sostener

Yo mejoré la disponibilidad de contexto y la ruta de validación de manera observable: yo pasé de no tener mapa, gate, checker ni workflow a tenerlos enlazados, ejecutables y comprobados. Yo protegí el mismo baseline funcional y evité copiar la implementación BEFORE al árbol de partida AFTER. Yo mantuve los 25 casos heredados y añadí diez casos del cambio controlado; yo incorporé quince pruebas de integridad del repositorio.

Yo calculé 61/100 BEFORE, 91/100 AFTER y una diferencia de +30 puntos. Yo asigné la puntuación con juicio de ingeniería y evidencia por dimensión. Yo no asigné 100/100 porque la CI remota, la independencia de sesiones y las decisiones semánticas humanas no quedaron demostradas por los scripts.

## Lo que yo no puedo atribuir causalmente

Yo observé cero preguntas de aclaración y cero cambios de producto fuera del alcance en ambas corridas. Yo no fabriqué una reducción. Yo conté únicamente lecturas de contexto explícitas; yo no usé el tiempo de ejecución, los tokens o una supuesta tasa de errores cognitivos como medidas porque no dispuse de instrumentación adecuada.

Yo mantuve el estado del agente entre condiciones y ejecuté una sola repetición por condición. Yo no presenté el texto oficial como si hubiera iniciado otra sesión autónoma. Yo necesité un ensayo independiente con sesiones limpias para medir reducción de exploración, preguntas o errores con validez causal.

## Riesgos y decisiones que yo conservo

Yo usé hashes como detección de cambios, no como autenticación frente a alguien que puede editar el checker y el manifiesto. Yo limité el control de secretos a nombres sensibles conocidos; yo no afirmé tener un scanner completo. Yo mantuve tags mayores de Actions y registré que no son pinning inmutable por SHA. Yo mantuve la aprobación humana para cambios de alcance, arquitectura, fuentes normativas y operaciones externas.

Yo conservaré AGENTS, REPO_MAP, el gate, la CI y las pruebas negativas como base de mi siguiente proyecto porque también me permiten incorporar a otro desarrollador sin explicaciones orales sobre rutas y comandos.

## Mi comparación cuantitativa observada

| Métrica que yo conté | BEFORE | AFTER | Interpretación que yo sostengo |
|---|---:|---:|---|
| Preguntas de contexto | 0 | 0 | Yo no observé reducción. |
| Archivos de contexto leídos explícitamente | 11 | 14 | Yo inspeccioné también mapa y automatización; yo no afirmé menos exploración. |
| Suposiciones incorrectas observadas | 0 | 0 | Yo no inferí razonamiento no registrado. |
| Fallos inesperados de comandos | 0 | 0 | Yo separé el red esperado de seis casos. |
| Archivos de producto fuera de alcance | 0 | 0 | Yo conservé el diff de dos archivos. |
| Casos de producto finales | 35 | 35 | Yo verifiqué el mismo comportamiento en ambas condiciones. |
| Casos adicionales del contrato | 0 | 15 | Yo añadí detección automática de incumplimientos de readiness. |
| Gate local de tres etapas disponible y aprobado | 0 | 1 | Yo comprobé una mejora operativa concreta. |

Yo almacené los mismos números en `results/evidence/run-metrics.json`. Yo no sumé las pruebas del contrato como si fueran funcionalidad adicional de Customer Search.
