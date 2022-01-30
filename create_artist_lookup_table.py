import pandas as pd
import json

df = pd.read_csv("./data/combined_pandas_df.csv")
artist_lookup_dict = {}
for id in df.artist_id.unique():
    artist_lookup_dict[str(id)] = df.loc[df.artist_id == id].clean_artist.values[0]

with open("./data/artist_lookup.json", "w") as outfile:
    json.dump(artist_lookup_dict, outfile)
