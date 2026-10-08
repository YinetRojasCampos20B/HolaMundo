# Proyecto HolaMundo
 
Primer proyecto con **Django** y **Python**. Muestra un "Hola mundo" en el navegador. Proyecto para las asignaturas Diseño UX/UI, Bases de Datos y Pruebas de Software. Nivel intermedio
 
## Requisitos
 
- Python 3.12.3 o una versión superior
- Sistema de control de versiones s Git

## ¿Cómo ejecutar el proyecto?
 
### 1. Clonar el repositorio
 
```bash
git clone https://github.com/YinetRojasCampos20B/HolaMundo.git
cd HolaMundo
```
 
### 2. Crear y activar el entorno virtual

Un entorno virtual nos permitirá instalar librerías del lenguaje de programación correspondiente, en nuestro caso Python, y además de usar una versión específica del lenguaje vinculado a ese proyecto, sin correr el riesgo de que por instalar librerías directamente se "rompa" alguna funcionalidad crítica del sistema operativo.
 
#### En distribuciones basadas en Linux o el sistema operativo Mac:
 
```bash
python3 -m venv venv
source venv/bin/activate
```
 
#### En sistemas operativos basados en Windows:
 
```bash
python -m venv venv
venv\Scripts\activate
```
 
Si funcionó, ustedes verán `(venv)` al inicio de la línea de la terminal.
 
> En distribuciones basadas en Linux, como Ubuntu, si falla la creación del entorno, es meritorio instalar antes: `sudo apt install python3-venv`
 
### 3. Instalar las dependencias

 Para instalar las dependencias de este pequeño proyecto, deben dentro de la terminal correr el comando:
```bash
pip install -r requisitosHolaMundo.txt
```
 
### 4. Configurar las variables de entorno

Una variable de entorno es como si fuera una caja secreta en donde se guarda información importante, como llaves de acceso u otros datos sensibles.
 
Deben copiar el archivo de ejemplo y poner su propia clave:
 
```bash
cp .env.example .env
```
 
Abren `.env` y reemplazan el texto de ejemplo:
 
```
SECRET_KEY=pon-aqui-tu-clave
```
 
> ¡IMPORTANTE!: El archivo `.env` **no se sube a GitHub** (está en `.gitignore`). Cada uno de nosotros crea el suyo.
 
### 5. Preparar la base de datos
> Por defecto, la base de datos que se crea usa el motor SQLite, de bases de datos relacionales.
 
```bash
python manage.py migrate
```
 
### 6. Encender el servidor
 
```bash
python manage.py runserver
```
 
Deben abrir <http://127.0.0.1:8000/> en el navegador. Para apagar el servidor, usen `Ctrl + C`.
 
## Estructura del proyecto
 
| Carpeta o archivo | Para qué sirve |
|---|---|
| `manage.py` | Herramienta de comandos del proyecto (servidor, apps, migraciones, pruebas) |
| `holaMundo/` | Configuración del proyecto (`settings.py`, `urls.py`) |
| `saludo/` | App con la vista que muestra el "Hola mundo" |
| `requisitosHolaMundo.txt` | Lista de librerías que se instalan con `pip` |
| `.env.example` | Ejemplo de las variables de entorno necesarias (consultar sección de variables de entorno para ver explicación)|
| `.gitignore` | Archivos que Git no sube (`venv/`, `.env`, etc.) |
 
## Trabajo en equipo

Si desean colaborar con el proyecto:
 
1. Antes de empezar a trabajar hacer `git pull`
2. Crea una rama propia mediante `git checkout -b nombre-del-cambio`
3. Al terminar de consolidar los cambios `git add .`, `git commit -m "sjslfsfdfdsjjdsf"` y `git push -u origin nombre-del-cambio`
4. En GitHub, abre un **Pull Request** para su revisión.
Si se instala una librería nueva, es importante actualizar la lista de dependencias antes de subir los cambios:
 
```bash
pip freeze > requisitosHolaMundo.txt
```

Listo.. >_>
