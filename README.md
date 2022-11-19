# Localoger

<p align="center">
<img src="./Img/logo.png">
</p>

Localoger es un keylogger local que te genera un archivo **.txt** con todas las palabras registradas

## REQUISISTOS:

* python3

* pip

## USO:

Primero tendremos que ejecutar CMD como administrador y ejecutar el siguiente comando:

```
pip install -r requirements.txt
```

Ahora convertiremos el keylogger en un ejecutable **.exe** con pyinstaller:

```CMD
cd C:\Users\%USERNAME%\AppData\Roaming\Python\Python37\Scripts

pyinstaller --onefile LA RUTA DEL ARCHIVO
```

Ahora iremos a la carpeta **C:\Users\%USERNAME%\AppData\Roaming\Python\Python37\Scripts**
y buscaremos dos carpeta con el nombre dist y build en dist esta nuestro ejecutable, lo ejecutamos.

Para finalizar el keylogger CTRL + C y ya tendremos nuestro archivo **.txt** en la carpeta dist.
