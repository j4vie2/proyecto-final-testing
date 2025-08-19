# Proyecto Final - Módulo Testing

Automatización de pruebas con Selenium

## Instrucciones para la Ejecución

### 1. Prerrequisitos

- Tener Python 3.3 o superior instalado.

### 2. Configuración del Entorno

Clona o descarga este repositorio y navega a la carpeta raíz del proyecto.

https://github.com/j4vie2/proyecto-final-testing

```bash
# Crear y activar un entorno virtual
# En Windows
python -m venv venv
.\venv\Scripts\activate

# En macOS/Linux:
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias

Instala todas las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
```

### 4. Ejecución

Para ejecutar todas las pruebas automatizadas, simplemente corre el siguiente comando desde la carpeta raíz del proyecto:

```bash
pytest -v
```

Para ejecutar las pruebas automatizadas y generar un reporte en html corre el siguiente comando desde la carpeta raíz del proyecto:

```bash
pytest -v --html=report.html 
```
