import pandas as pd
import requests
import json

df = pd.DataFrame()
for i in range(1, 500):
    print(i)
    response = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US&page={}'.format(i))
    temp2_df = pd.DataFrame(response.json()['results'])[['id', 'title', 'original_title', 'popularity', 'release_date', 'overview']]
    df = df.append(temp2_df,ignore_index=True)
df.to_csv("movies.csv")

