# App Web Interactiva
Esta aplicación se llevo a cabo con phyton, streamlit y Plotly, por lo que permite analizar los datos plasmados en el dataset a traves de distintos gráficos.

El objetivo de este proyecto es ofrecer una herramienta sencilla y visual en el que se puedan mostrar datos según el interes de cada usuario. En el detalle de la app tenemos lo siguiente:

1. Se genera una vista previa de los datos en el que nos basamos para el desarrollo general.

2. Analizamos mediante un histograma los vehículos por modelo según el tipo al que corresponde, por ejemplo, si quisieramos ver los modelos que tiene el tipo de vehículos "mini-van" al darle un solo clic sobre el tipo en la leyenda lateral me mostrara la cantidad de estos por modelo. 
3. Visualizamos los tipos de vehiculos con el total de ventas por cada año. 

Esta app se utilizo mediante las siguientes librerias:
- Streamlit: me permitió crear la interfaz web interactiva.
- Potly Express: ejecutó las visualizaciones gráficas.
- Pandas: manipulación y agrupación de datos. 

El proyecto está configurado para desplegarse automaticamente en Render.com.

El proyecto se encuentra estructurado de la siguiente forma:

PROJECT/
|
|-app.py #Código principal 
|-requirements.txt #librerías necesarias
|-.phyton-version #se creó para almacenar la versión de phyton
|-README.md #Descripción del proyecto
|-vehicles_env #Entorno virtual 
|-vehicles_us.csv #dataset utilizado para el desarrollo del proyecto.
|-notebooks #prueba
