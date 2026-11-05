# ADA-07 - Build an Agent Skill

Entrega técnica preparada sobre el repositorio del estudiante. Incluye Skill propia, Skill profesional completa y fijada, evaluaciones asistidas, evidencia ejecutada, comparación, bitácora y reflexión técnica para revisión personal.

## Alcance y estado
Repositorio: https://github.com/Javier-de-Jesus-Ortiz-Miss/ada-05-spec-driven-feature.
Base: 8ab0a4f5f34804a2dc24c4b87a1aa5a2efdaabb5.
Head: 0bfa0b8836589366b0dd6fb6ceada326d7fa5a87 (test/search-edge-cases).
Se evaluó el diff agregado desde especificación hasta feature y tests ampliados; no se inventó un PR ni se escribió a GitHub. project/ conserva una copia del código en ese head.

Comprobado: 25 tests del proyecto; 28 tests del validador; 3 reportes válidos; build/CLI instalable; 5 mutaciones aisladas; metadata; integridad de fuente y colección profesional. 9 prompts clasificados por el LLM en esta sesión.
Pendiente: discovery automático de ambas Skills en sesión nueva y lectura/decisión personal del estudiante. Los 9/9 asistidos no sustituyen un test del router nativo. Ver docs/definition_of_done.md.

## Contenido de entrega
- .agents/skills/reviewing_pull_requests/: Skill original 1.0.1 y recursos obligatorios.
- .agents/professional/agent-skills/: colección completa de Addy Osmani, commit fijo; .agents/skills/ contiene enlaces descubribles a sus Skills.
- docs/: observación, auditoría, anatomía, estudio profesional, reflexión y Definition of Done.
- results/: reviews, evaluación, comparación y logs reales.
- AI_USAGE_LOG.md: diez entradas con autoría/decisiones diferenciadas.
- tools/: pruebas del validador y verificación reproducible de entrega.
- output/pdf/ADA-07_Informe.pdf: informe de lectura integrado.

## Reproducir pruebas
Desde la raíz de ada-07-agent-skill, con Python 3.11+:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r tools/requirements-evaluation.txt
(cd project && PYTHONDONTWRITEBYTECODE=1 python -m pytest -v -p no:cacheprovider)
PYTHONDONTWRITEBYTECODE=1 python -m pytest tools/test_validator.py -v -p no:cacheprovider
python .agents/skills/reviewing_pull_requests/scripts/validate_review_report.py results/pr-readiness-review.md
python tools/verify_delivery.py
```

No instalar dependencias de la colección profesional ni ejecutar sus hooks para esta práctica. La fuente y scripts de tests se inspeccionaron antes de ejecutar. Los logs registran el entorno temporal usado en la ejecución original; rutas temporales no son dependencias de la entrega.

## Recarga y prueba de discovery que falta
Abrir una nueva conversación del coding agent desde esta carpeta, recargar Skills según el host y verificar que estén disponibles reviewing-pull-requests y code-review-and-quality. La carpeta reviewing_pull_requests conserva la convención del curso aunque name utiliza guiones. Si el host requiere otra ruta, documentar el cambio y mantener la estructura.

Prompt positivo: `Review the local change in project from 8ab0a4f to 0bfa0b8 against requirements and tests. Create a draft review locally. Do not write to GitHub.`
Prompt negativo en otra conversación: `Explain what a pull request is.` No debe activar reviewing-pull-requests.
Prompt profesional: `Use code-review-and-quality to review the same local change. Do not modify project code or write to GitHub. Produce results/professional-skill-review.md.`
Registrar discovery real y actualizar evaluation report / Definition of Done. No reescribir logs previos como si fueran una sesión nueva.

## Revisión humana
Leer informe, Skill y evidencias; aceptar o rechazar sugerencias y personalizar reflexión/bitácora si corresponde. No están autorizados comment/approve/merge ni cambios en la feature. La conclusión personal no se firma automáticamente.

## Instalación de terceros
Método alternativo a npx: clonación/copia completa fijada antes de uso y enlaces locales relativos, conservando references compartidas. Se evita ejecutar otro instalador; upstream documenta integración por clone. LICENSE y manifest SHA-256 incluidos. Ningún plugin/hook global habilitado ni autoactualización.

## Portabilidad del ZIP
Los enlaces de Skills de terceros se materializan como carpetas normales en el ZIP y se incluyen referencias compartidas en .agents/references/. La colección original fijada permanece íntegra en .agents/professional/agent-skills/. Esto permite extraer sin depender del soporte de enlaces simbólicos. No se incluyen .git, entornos virtuales ni cachés.
