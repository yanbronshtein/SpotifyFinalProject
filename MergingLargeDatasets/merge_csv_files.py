import polars as pl
full_df = pl.read_csv('../data/unprocessed.csv')
freq_df = pl.read_csv('../data/combined_pandas_df.csv')
joined_df = freq_df.join(full_df, on='user_id', how='inner')
joined_df.to_csv('../data/polars_join.csv', has_headers=True)