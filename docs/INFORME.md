# TP Semana 3 - Automatización de calidad
Autor: Michael Chiappone
Estado: preparación práctica; NO certificado para integración.

## 1. Pre-commit
El script .githooks/pre-commit verifica Black, Ruff y pytest, en ese orden. Cada fallo muestra el diagnóstico, devuelve un código distinto de cero y cancela el commit. Los pasos posteriores no se ejecutan. Los archivos permanecen disponibles para corregirlos. Black --check no modifica archivos; para corregir el formato usar python -m black src tests y luego git add.
El hook reduce errores locales, pero puede omitirse: la protección de main requiere además revisión y controles obligatorios en el servidor.

## 2. Auditoría estática
Analizar complejidad ciclomática por función, duplicación, bugs, deuda técnica y dependencias. Extraer lógica repetida, dividir responsabilidades y usar retornos tempranos, conservando pruebas del comportamiento. Actualizar dependencias vulnerables a versiones compatibles corregidas y repetir pruebas y escaneo.
Este proyecto pequeño sirve para practicar los controles. No constituye todavía el caso de código degradado con duplicaciones, alta complejidad y dependencias desactualizadas exigido por el punto 2. Debe agregarse ese caso y comparar mediciones antes/después. Radon sirve como complemento; no reemplaza el diagnóstico SonarQube solicitado en el material.

## 3. Evidencias pendientes para el Informe en Verde
- Enlace real al Issue: PENDIENTE.
- Enlace real al PR y referencia al Issue: PENDIENTE.
- Commit evaluado y fecha: PENDIENTE.
- Logs del hook ejecutado por git commit: PENDIENTE.
- Reporte de cobertura de ese commit: PENDIENTE de ejecución local.
- Diagnóstico SonarQube y comparación antes/después: PENDIENTE.
- Escaneo actualizado de dependencias: PENDIENTE.
- Revisión por pares: PENDIENTE.
- Evidencias del TP 2: PENDIENTES de incorporar.

No declarar aptitud hasta cumplir la DoD y adjuntar las evidencias. Los resultados deben corresponder al mismo código. Conservar reportes junto con el hash del commit; un archivo de log por sí solo no es inmutable.

## Validación realizada en el entorno del asistente
Fecha: 27/09/2026. Python 3.12.14. Ejecución directa del script del hook con sh, no mediante un commit del alumno. Black y Ruff aprobados; 12 pruebas pytest aprobadas; cobertura de sentencias y ramas: 100 %. Ver evidencias/validacion-entorno-asistente.txt, coverage.xml y htmlcov/index.html. Esto no reemplaza la trazabilidad del PR, SonarQube ni el escaneo de dependencias pendientes.
