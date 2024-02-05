# Ensurance LR 
Repositorio con los archivos de trabajo del primer proyecto de Inteligencia Artificial sobre los modelos de Regresión Lineal en el campo del Machine Learning.

## Preparando el entorno virtual
Para evitar problemas de compatibilidad entre las arquitecturas de los diferentes sistemas operativos que puede utilizar cada uno en su casa (*principalmente Windows, MacOS y GNU/Linux*) no he incluido el entorno virtual configurado dentro del repositorio. Además, al tener un alto peso por la cantidad de archivos que contiene también es conveniente no tenerlo presente para reducir los tiempos de descarga.

Como con cualquier otro proyecto que realicemos con el lenguaje de programación Python, es una buena práctica crear un entorno virtual aislado de la versión de Python del sistema para manejar las dependencias de forma interna por proyecto. Esto ayuda a evitar posibles problemas de compatibilidad entre dependencias porque ciertas versiones actualizadas no sean compatibles con las anteriores. No hace falta que entendamos todo esto, pero lo importante es saber inicializar el entorno virtual:

Para ello, tendremos que ejectuar el siguiente comando, independientemente del tipo de **terminal** que estemos utilizando:
(*El símbolo del $ NO se debe escribir junto con el comando, es sólo representativo de que estamos en la terminal*)

```shell
$ python -m venv <nombre del entorno virtual>   # En windows también se puede poner como py -m venv <nombre del entorno virtual>
# Ejemplo: python -m venv mi-entorno
```

Este comando crea un nuevo **entorno virtual** de Python que podemos utilizar a través del siguiente comando:

```shell
$ .\Scripts\activate    # Windows
$ source bin/activate   # MacOS y GNU/Linux 
```

Nótese que estos comandos se ejecutan suponiendo que el usuario se encuentra en el directorio del repositorio clonado. Es decir, que los ejecutamos desde el directorio `ensurance-lr` que estará localizado en diferentes rutas dependiendo de dónde hayamos clonado el repositorio.

Ahora que ya hemos activado el entorno virtual, es hora de instalar todos las librerías o dependencias necesarias para ejecutar tanto el cuaderno de Jupyter como la aplicación web que implementa el modelo de Regresión Lineal. 

## Instalando dependencias

Podríamos instalar un listado de dependencias escribiendo su nombre detrás del comando `pip install` que siempre se ejecuta en terminal para instalar librerías en Python. Sin embargo, hay una forma mucho más eficiente y sencilla de instalar un conjunto concreto de librería.

Para ello, el gestor de paquetes de Python (*la herramienta con la que instalamos las librerías que necesitamos en nuestros proyectos*) cuenta con un *subcomando* o *función* que devuelve un listado de todas las librerías que están instaladas para la versión de Python activa en el entorno de trabajo. Esto es, para nuestro caso, las librerías que tenemos instaladas dentro de nuestro entorno virtual. Esta es la función `freeze`.
Esto sólo devuelve un listado de librerías que se muestra por consola, para poder escribirlo a un archivo, se utiliza algo que se conoce como operador de redirección del la salida estándar (*stdout redirection operator*) pero no hace falta conocer ese concepto, porque es más complejo.
Resumiendo, que para obtener un listado con las librerías que tenemos en el entorno virtual ejecutaríamos el siguiente comando:

```shell
$ pip freeze > <nombre del archivo de dependencias>.txt
# Ejemplo: pip freeze > requirements.txt
```

Normalmente al archivo se le pone el nombre de *requirements* porque representa las dependencias del proyecto.
Este archivo ya lo he creado yo, pero está bien saberlo para poder hacer migraciones entre ordenadores o para no tener que instalar todo de cero al iniciar un proyecto parecido.

Este archivo nos sirve ahora para instalar todas esas librerías de una sola pasada, ejecutando el siguiente comando:

```shell
$ pip install -r <nombre del archivo de dependencias>.txt
# Ejemplo en nuestro caso: pip install -r requirements.txt
```

Lo que indica la `-r` que se conoce con el nombre de *flag* o "*bandera*" en su traducción literal, es que en lugar de instalar una librería concreta, quieres instalar todas las librerías que haya listadas dentro del archivo que hemos creado con `pip freeze`.

Si hemos hecho todo este proceso correctamente, ya tendremos configurado el entorno virtual con las dependencias necesarias para ejecutar la web y el cuaderno. 

## Ejecutando los archivos

Este es el último paso y más sencillo de todos, inspeccionar y ejecutar los archivos más importantes del proyecto: `app.py` y `proyecto-final.ipynb`. Para ello, utilizaremos VSCode. Si queremos abrir VSCode con el directorio en el que estamos ahora mismo (el del proyecto), simplemente tenemos que ejecutar el siguiente comando:
```shell
$ code .
```

Lo que le indica al sistema operativo este comando es que queremos abrir VSCode con la carpeta o directorio con el que estemos trabajando actualmente en la terminal. Eso es lo que representa el punto `.`.

Una vez se haya abierto VSCode, para ver los archivos simplemente habrá que *clicar* sobre ellos e inspeccionar el código.
En el caso del cuaderno se van ejecutando las celdas de forma secuencial para ir obteniendo las diferentes salidas (*probablemente os pedirá que instaléis unas extensiones relacionadas con los cuadernos de Jupyter, bastará con instalarla y luego la extensión os irá guiando para ejecutar las celdas utilizando la versión de Python que hemos configurado antes en el entorno virtual*).
En el caso de la aplicación web, tendremos que utilizar la herramienta de terminal de `streamlit` para ejecutarla. Como siempre, el comando que se utilizaría sería el siguiente:

```shell
$ streamlit run app.py
```

Y ya está, con todo esto hecho deberías poder interactuar localmente con la aplicación web y también investigar y cacharrear con el cuaderno de Jupyter en el que se entrena el modelo.
Happy Coding :)
