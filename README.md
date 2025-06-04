
#Proyecto individual 1 - datapt03 - Gonzalo Ducca

## Introducción

En este proyecto se trabaja sobre base de datos relativas a una empresa de videojuegos. Los datos describen juegos, usuario y sus reviews. Se realiza una exploración, transformación y visualización de datos. Se construyen funciones que serán mostradas en una API a la cual se le aplicará un deploy. Además, se realiza un modelo de recomendación. 

### Transformaciones

Se eliminaron columnas que tenían gran cantidad de datos nulos y columnas que no eran relevantes para el análisis. Se desanidaron datos que tenían fomato lista. Se eliminaron duplicados. 
Esto está en archivos que comeinzan con ETL

### Visualización

Se realizó el EDA de la base de datos referida a los juegos y a lo último se visuaiza un gráfico de barras mostrando una distribución de los datos de la columns 'Géneros'.
Está en archivo "ETL.games"

### Modelo de aprendizaje automático

Se creó un modelo de recomendación "recommend_games_by_id(id)" a la cual se le ingresa el id de un juego y devuelve una lista con 5 juegos recomendados similares al ingresado (relación item-item).

Para medir la similitud entre los juegos se utilizó la "similitud del coseno". 

Está en archivo "main"

### API

* **countreviews**: `Cantidad de usuarios` que realizaron reviews entre las fechas dadas y, el `porcentaje` de recomendación de los mismos en base a reviews.recommend.

* **genre**: Devuelve el `puesto` en el que se encuentra un género sobre el ranking de los mismos analizado bajo la columna PlayTimeForever.

* **userforgenre**:
    `Top 10` de usuarios con más horas de juego en el género dado, con su URL (del user) y user_id.

* **recomendacion_juego**: Esta función recibe como parámetro el id de un juego y devuelve una lista con 5 juegos recomendados similares al ingresado.

Todo esto está en archivo "main"

### Deploy
https://gonzaloduccapi1.onrender.com/docs
