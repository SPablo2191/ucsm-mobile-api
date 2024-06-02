## Tecnologias 👨‍💻
![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Django](https://img.shields.io/badge/Django-4.0-brightgreen.svg)
![Rest Framework](https://img.shields.io/badge/Rest_Framework-3.14.0-brightgreen.svg)

## Entornos Compatibles 💻
![macOS](https://img.shields.io/badge/macOS-compatible-green)
![Linux](https://img.shields.io/badge/Linux-compatible-green)
![Windows](https://img.shields.io/badge/Windows-compatible-green)

## Instalación🤖
Para hacer uso del proyecto de manera local se puede realizar de 2 formas distintas:
### Uso de docker:
1) crear .env en directorio raiz con el siguiente formato:
```json
DB_USER = postgres
DB_PASSWORD = postgres
DB_HOST= db
DB_PORT= 5432
DB_NAME= postgres
```
Se usa un package para leer dicho archivo y cargarlo en el settings.py del proyecto
2) Se debe disponer [docker engine](https://docs.docker.com/engine/install/) en la computadora ya sea usando [windows](https://docs.docker.com/desktop/install/windows-install/) o [linux](https://docs.docker.com/desktop/install/linux-install/) y ejecutar el siguiente comando:
```cmd
docker-compose up --build
```
3) a continuación en la terminal del servicio web debemos ejecutar los siguiente comandos:
```bash
python src/manage.py migrate
```
Que realizara la migraciones corespondientes en la bdd; y el siguiente comando:
```bash
python src/manage.py createsuperuser
```
Para tener un usuario que pueda acceder al menu de administración de django.
4) Listo! Ya se puede acceder a la instancia

### Con entorno virtual y base de datos psql
1) Ingresar los siguiente comandos en consola:
```cmd
python3 -m venv [nombreDelEntornoVirtual]
```
este comando les creara un entorno virtual para para poder importar posteriormente los paquetes ahi.Para activarlo se emplea el siguiente comando:

```cmd
source nombreDelEntornoVirtual/bin/activate
```
NOTA: en caso de trabajar con windows el entorno virtual se genera con scripts para activar el entorno virtual por ende se tiene que acceder de la siguiente forma:
```cmd
nombreDelEntornoVirtual\Scripts\activate.bat
```
y para apagarlo (en ambos casos) es:

```cmd
deactivate
```

2) despues correr el siguiente comando para obtener los paquetes empleados en la API:

```cmd
pip install -r requirements/dev.txt
```
3) crear un archivo .env en el directorio raiz con el siguiente formato:
```json
DB_USER = [Nombre de usuario ej: postgres]
DB_PASSWORD = [Contraseña a poner ej: postgres]
DB_HOST= [host del servicio ej:localhost]
DB_PORT= [puerto que escucha de la bdd ej: 5432]
DB_NAME= [nombre de la db ej:postgres]
```
Se usa un package para leer dicho archivo y cargarlo en el settings.py del proyecto
4) Una vez los paquetes fueron instalados con exito, se debe realizar las migraciones:
```cmd
python src/manage.py migrate
```
5) Crear un superusuario para acceder al modulo admin:
```cmd
python src/manage.py createsuperuser
```
6) Levantar el servidor:
```cmd
python src/manage.py runserver
```
6) ¡Listo! ya puede visitar la pagina web en este [enlace](http://127.0.0.1:8000/).