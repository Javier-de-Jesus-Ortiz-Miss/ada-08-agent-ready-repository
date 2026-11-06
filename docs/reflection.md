# Mi reflexión individual

## 1. Mi principal obstáculo en BEFORE

Yo encontré una validación incompleta a nivel repositorio: yo podía correr pytest, pero yo no tenía un comando que comprobara simultáneamente comportamiento, estilo y contratos.

## 2. El conocimiento que yo tuve que inferir

Yo tuve que relacionar el invariante de identificador en SPEC con el constructor y las pruebas. Yo también tuve que decidir cómo distinguir evidencia histórica de resultados actuales.

## 3. La mejora de mayor impacto para mí

Yo elegí verify_repo como la mejora operativa más importante porque yo convertí tres obligaciones dispersas en un resultado con código de salida verificable. Yo no afirmé que su impacto causal sobre el agente estuviera medido por una sesión independiente.

## 4. El contenido que yo reservé para AGENTS

Yo incluí fuentes, rutas, comandos, límites y DoD. Yo dejé fuera la definición de requisitos y el detalle arquitectónico porque yo ya tenía fuentes específicas para ellos.

## 5. La regla que yo convertí en software

Yo convertí la preservación de evidencia y datos protegidos en comparación SHA-256 con cobertura exacta. Yo probé tanto una modificación real como un intento de quitar una entrada del manifiesto.

## 6. Mi diferencia entre más contexto y mejor contexto

Yo entendí mejor contexto como información localizada en el momento de decidir: yo añadí una tabla por pregunta y un contrato breve, en lugar de repetir toda la especificación en varios archivos.

## 7. El riesgo de duplicar instrucciones por herramienta

Yo detecté que dos copias de los requisitos pueden divergir. Yo preferí un contrato común y preservé la skill histórica como referencia, sin inventar una nueva autoridad normativa.

## 8. Los checks que yo compartí

Yo compartí pytest, Ruff y check_repo_contract a través del mismo script. Yo hice que CI invocara ese script sin copiar su lógica.

## 9. La decisión que yo mantuve humana

Yo reservé cambios semánticos de requisitos, expansión de arquitectura, operaciones destructivas y acciones externas para una decisión humana explícita. Yo no sustituí esas decisiones con una prueba verde.

## 10. La evidencia de mejora que yo acepté

Yo acepté la presencia y ejecución del gate, la protección negativa comprobada, el mapa enlazado y la comparabilidad de fuentes. Yo separé esas mejoras de una reducción de preguntas o errores que no pude demostrar.

## 11. La mejora que yo compartiría con alguien nuevo

Yo usaría REPO_MAP para mostrar dónde cambia cada comportamiento y qué prueba ejecutar. Yo evitaría depender de mi memoria para explicar el repositorio.

## 12. Mi variable no controlada

Yo mantuve el estado del agente entre BEFORE y AFTER. Yo también tuve una sola corrida por condición y no ejecuté la matriz remota. Yo marqué esos límites en la evaluación experimental.

## 13. Lo que yo conservaré para el proyecto final

Yo conservaré AGENTS, REPO_MAP, la trazabilidad, el gate, las pruebas negativas y la distinción entre evidencia automática y revisión humana. Yo repetiré el experimento en sesiones limpias si necesito sostener una comparación de desempeño del agente.
