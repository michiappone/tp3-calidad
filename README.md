# TP Semana 3 - Calidad de pedidos
Proyecto inicial para Michael Chiappone. Calcula precio unitario en centavos por cantidad; rechaza entradas inválidas. No requiere base de datos ni servidor. El total 450000 representa $4500,00.

## Primer paso en Windows / VS Code
Extraer el ZIP y abrir esta carpeta en VS Code. Abrir una terminal PowerShell y ejecutar:
```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m black src tests
.\.venv\Scripts\python.exe -m ruff check src tests
.\.venv\Scripts\python.exe -m pytest
```
Abrir htmlcov/index.html para ver la cobertura. Se exige un mínimo del 80 %. Las dependencias no están fijadas a versiones: al instalar, guardar las utilizadas con pip freeze para reproducir el entorno.

## Activar y probar el hook (terminal Git Bash)
```bash
source .venv/Scripts/activate
git init -b main
git config core.hooksPath .githooks
chmod +x .githooks/pre-commit
python -m black src tests
git add .
set -o pipefail
git commit -m "Agrega proyecto de pedidos y controles de calidad" 2>&1 | tee evidencias/pre-commit-local.txt
git rev-parse HEAD > evidencias/commit-evaluado.txt
python -m pip freeze > evidencias/versiones.txt
```
Si Git solicita identidad, configurar tu nombre y correo. Si falla el commit, corregir primero y repetir; no omitir el hook. El log se genera durante el commit y queda fuera de ese commit: conservarlo como evidencia asociada al hash, sin afirmar que estaba contenido en él.

## Análisis complementario
```bash
python -m radon cc src -s -a > evidencias/complejidad.txt
python -m pip_audit -r requirements-dev.txt > evidencias/dependencias.txt 2>&1
```
El escaneo necesita internet. Si falla la consulta, no equivale a cero vulnerabilidades. No instalar versiones vulnerables deliberadamente para construir el ejemplo.

## GitHub y SonarQube: pasos posteriores
Crear un repositorio en GitHub y subir la base. Crear un Issue real con la plantilla, luego una rama para resolverlo y un PR hacia main. Vincular el PR con el número real del Issue y solicitar revisión a un compañero. No inventar enlaces ni aprobaciones.
Para SonarQube local se incluye sonar-project.properties: generar coverage.xml con pytest, configurar el servidor y scanner, y ejecutar el análisis autenticado. No guardar tokens en el repositorio. Adjuntar el reporte real.

## Alcance
Este ZIP es la base ejecutable, no la entrega final certificada. Leer docs/INFORME.md para los requisitos pendientes, especialmente la auditoría antes/después y las evidencias de los prácticos anteriores.

Validación incluida: Black y Ruff aprobados, 12 pruebas aprobadas y 100 % de cobertura en el entorno del asistente. El ZIP contiene el reporte HTML. Repetir en tu computadora para generar evidencia local.
