# Tech Interview

Este proyecto es una API construida en [Flask](https://flask.palletsprojects.com/en/2.1.x/) para la entrevista ténica de Globant

* Parámetros a seguir:
* * Soporte para el endpoint `GET /allBerryStats`
* * Debe retornar:
```
{
    "berries_names": [...],
    "min_growth_time": "" // time, int
    "median_growth_time": "", // time, float
    "max_growth_time": "" // time, int
    "variance_growth_time": "" // time, float
    "mean_growth_time": "", // time, float
    "frequency_growth_time": "", // time, {"growth_time": frequency, ...}
}
```
* * El reponse debe tener la cabecera "content-type" (application/json)

En orden de mantener privacidad y no es relevante para probar este proyecto, no incluiré otros parámetros que me han sido asignados a seguir.

## Instalación

Clonar el proyecto como normalmente clonas un proyecto de github.

```
$ git clone https://github.com/Brixt18/GlobantTechInterview
```
O descargando el archivo .zip del mismo.

Una vez clonado el proyecto, **Crear** dentro de la carpeta `app/config` un archivo `.env` con las variables de entorno.
```
SECRET_KEY=MySuperSecretKey
```

Debería quedar un arbol así:
```bash
└───app
    ├───api
    │   └───...
    ├───config
    │   └───.env
    ├───utils
    │   └───...
    └───...
```


## Requisitos
* [Python >= 3.7](https://www.python.org/downloads/release/python-370/)

## Dependencias
Para probar en un entorno virtual, utilizar [venv](https://docs.python.org/3/library/venv.html) de Python.

Dentro de la carpeta del proyecto, ejecutar:
```
$ python -m venv .venv
```
### Acitvar el virtual-env
* Windows
```
$ cd .venv/scripts
$ activate
(.venv) $ cd ..
(.venv) $ cd ..
```
* Linux
```
$ source .venv/bin/activate
(.venv) $
```

## Instalar Dependencias
Instalar usando pip
```
(.venv) $ pip install -r requirements.txt
```

## Cómo Usar

### Inicializar
Una vez instaladas todas las dependencias, ejecutar el archivo `run.py`
```
(.venv) $ python run.py
```
Y la aplicación comenzará a ejectuar en entorno Local con el puerto 5000 (`localhost:5000`).

## Probar

### Localmente
Para verificar el enpoint, abrir en su navegador de preferencia, mientras al aplicación está ejecutandose, la URL: `localhost:5000/allBerryStats`, y esta debería retonar un JSON con los parámetros establecidos anteriormente.

### Internet
La aplicación tiene un deploy hecho en Heroku: [TechInterview-Heroku](https://globant-tech-interview.herokuapp.com/allBerryStats/)
(https://globant-tech-interview.herokuapp.com/allBerryStats/) 