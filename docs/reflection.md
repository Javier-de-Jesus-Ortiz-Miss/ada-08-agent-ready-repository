# Reflexión — ADA-05

1. **¿Qué diferencia hay entre requirement, specification y prompt?**

   El requirement describe una necesidad que debe resolver el programa. La specification detalla cómo debe comportarse la solución y cómo comprobar que cumple esa necesidad. El prompt es la instrucción que se le da a la IA para realizar una tarea. En este proyecto, buscar clientes por correo es un requisito; aceptar coincidencias parciales y definir la respuesta cuando no hay resultados forma parte de la especificación.

2. **¿Qué información fue indispensable antes de programar?**

   Fue necesario definir los datos de cada cliente, los campos de búsqueda y el comportamiento esperado ante entradas vacías o búsquedas sin coincidencias. También debía quedar claro el alcance del proyecto. Esa información permitió orientar la implementación y establecer qué resultados se considerarían correctos.

3. **¿Qué decisiones debieron resolverse antes de programar?**

   Se definió utilizar una CLI con clientes ficticios en memoria. Aprobé esta propuesta porque permite demostrar la búsqueda sin añadir una base de datos o una interfaz web. También quedaron establecidas las coincidencias parciales, la comparación sin distinguir mayúsculas y la conservación del orden de entrada.

4. **¿Qué errores evitó SPEC.md?**

   Ayudó a evitar interpretaciones distintas sobre el comportamiento de la búsqueda. Por ejemplo, establece que no encontrar clientes es un resultado válido, mientras que introducir un término vacío es un error. También aclara que un cliente que coincide por nombre y correo debe aparecer una sola vez.

5. **¿Qué problema evita separar REQUIREMENTS.md de SPEC.md?**

   Evita mantener varias definiciones de un mismo requisito. `REQUIREMENTS.md` concentra las necesidades del producto y `SPEC.md` las referencia mediante sus identificadores para describir reglas y criterios de aceptación. Esto facilita localizar un cambio y revisar qué partes del proyecto podrían verse afectadas.

6. **¿Qué papel tuvo AGENTS.md?**

   Funcionó como una guía para el trabajo del agente. Indicó qué documentos debía consultar, cómo seguir las tareas y qué verificaciones realizar. También estableció límites, como no modificar los requisitos para hacer pasar las pruebas ni eliminar pruebas que detectaran problemas.

7. **¿Qué cambió durante la revisión humana?**

   Leí y aprobé los documentos y la implementación, y confirmé esa revisión al cierre. Mantuve el alcance y el comportamiento presentados. Aporté ideas y ajustes para explicar mejor el trabajo y mi participación, y la IA ayudó a redactarlos. La corrección técnica del README y la ejecución de las pruebas fueron realizadas por Codex.

8. **¿La arquitectura coincidió con el código final?**

   Sí. El código conserva la separación entre el modelo de cliente, los datos de ejemplo, la búsqueda y la CLI. Cada módulo tiene una responsabilidad concreta. La función de búsqueda devuelve resultados sin imprimirlos, mientras que la CLI recibe los argumentos y muestra la respuesta. Esto permite probar la lógica con diferentes datos.

9. **¿Qué requisito fue más difícil de probar?**

   Considero que NFR-02 requirió una verificación más amplia, porque comprobar la ejecución local no depende únicamente de obtener una respuesta correcta. También hay que revisar que el código no necesite servicios externos ni credenciales. La aplicación utiliza la biblioteca estándar de Python durante su ejecución; `pytest` se utiliza para las pruebas.

10. **¿Qué mejorarías en tu proceso spec-driven?**

    Verificaría los permisos y el funcionamiento de `agy` antes de iniciar la implementación. También guardaría el reporte de cada tarea y registraría las revisiones conforme se realizan. Así sería más fácil identificar qué terminó el agente, qué problemas encontró y qué decisiones se aprobaron en cada momento.

11. **¿Por qué SPEC.md puede funcionar como contrato verificable sin duplicar los requisitos?**

    Porque relaciona cada requisito con comportamientos observables y criterios de aceptación. Por ejemplo, FR-06 se comprueba mediante entradas vacías o compuestas por espacios, junto con el mensaje y el código de salida correspondientes. La especificación permite verificar ese comportamiento utilizando el ID del requisito, sin volver a definirlo.

12. **¿Qué decisiones importantes aparecen en tu AI Usage Log y cómo cambió tu criterio después de revisar las sugerencias de la IA?**

    El registro incluye la propuesta de requisitos, el uso de una CLI con datos en memoria, la separación de la búsqueda y la comparación mediante `casefold()`. Las propuestas dieron una forma concreta al objetivo general del ADA. Leí y aprobé el contenido presentado, manteniendo el alcance de una solución pequeña y verificable. La IA redactó los documentos, implementó el código y ejecutó las pruebas; mi revisión y aprobación quedaron registradas al cierre.