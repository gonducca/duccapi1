import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from fastapi import FastAPI 
from sklearn.metrics.pairwise import cosine_similarity
 
dfgenre2=pd.read_parquet('genre.parquet')
archivo="user_reviews.parquet"
user_reviews= pd.read_parquet(archivo)
ufg= pd.read_parquet('userforgenre.parquet')
df_modelo=pd.read_parquet(r'df_modelo.parquet')
similitudes = cosine_similarity(df_modelo.iloc[:,3:])

app=FastAPI()

# La siguiente función retorna la cantidad de usuarios que realizaron reviews y el porcentaje de reviews de estos con respecto al total de usuarios en un ranfo de fechas
"""
Parametros:
        -f_inicio(str/datetime): Fecha de inicio del rango a evaluar 
        -f_final(str/datetime): Fecha final del rango a evaluar 
Retorna
        -Cantidad de usuarios: con reseñas dentro de ese período de tiempo
        -Porcentaje de reviews entre fechas : del usuario con respecto al total en el período
"""
@app.get("/")
def pagppal():
    return {"Bienvenido"}

@app.get("/countreviews/{f_inicio}/{f_final}")
async def countreviews(f_inicio,f_final):
    #convierte las fechas a objetos datetime en el caso de que no lo estén
   
    #crea el rango de fechas mediante el filtro
    rango_fechas=user_reviews[(user_reviews['posted']>=f_inicio)&(user_reviews['posted']<=f_final)]
    
    #calculo de la cantidad de usuarios que hicieron reviews entre esas fechas
    count_usu= rango_fechas["user_id"].nunique()
    
    #calculo el porcentaje de reviews en el mismo rango
    porcentaje_fechas=(rango_fechas["recommend"].sum() / len(rango_fechas))* 100
    
    return{
        "Cantidad de usuarios con reseñas" : count_usu ,
        "Porcentaje de reviews entre fechas": round(float(porcentaje_fechas), 3)
    }

@app.get("/genre/{genero}")
async def genre(genero):
    
    puesto = dfgenre2[dfgenre2['genres'] == genero]['Puesto'].iloc[0].item()
    
    return {'El género': genero, 
            'se encuentra en la posición': puesto
    }

@app.get("/userforgenre/{genero}")
async def userforgenre(genero):
 mask = ufg[ufg['genres'] == genero]

    # Tomar los primeros 5 registros del DataFrame
 top5 = mask[['user_id', 'user_url', 'playtime_forever']].head(5).reset_index(drop=True)

 return  {'El TOP 5 de usuarios para el género' : genero, 
             'es el siguiente' : top5}

@app.get("/recommend_games/{id}")
def recommend_games_by_id(id):
    
    # Obtiene las puntuaciones de similitud del juego con todos los demás
    game_similarities = similitudes[id]
    
    # Enumera los juegos y sus similitudes correspondientes
    similar_games = list(enumerate(game_similarities))
    
    # Ordena la lista de juegos similares en función de las similitudes
    similar_games = sorted(similar_games, key=lambda x: x[1], reverse=True)
    
    # Selecciona los 10 juegos más similares (puedes cambiar este número según tus preferencias)
    top_similar_games = similar_games[1:11]  # Excluye el juego en sí mismo
    
    # Obtiene los títulos de los juegos recomendados
    for game in top_similar_games:
        index = game[0]  # Obtener el índice del juego similar
        title = df_modelo.iloc[index]['title']  # Obtener el título del juego
        recommended_games_dict[index] = title  # Agregar el título al diccionario con el índice como clave

    return recommended_games_dict 
