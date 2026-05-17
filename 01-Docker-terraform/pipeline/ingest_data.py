#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

possible_dates = [
    "tpep_pickup_datetime", "tpep_dropoff_datetime",
    "lpep_pickup_datetime", "lpep_dropoff_datetime"
]


@click.command()
@click.option("--pg-user", default="root", show_default=True, help="Postgres username")
@click.option("--pg-password", default="root", show_default=True, help="Postgres password")
@click.option("--pg-host", default="localhost", show_default=True, help="Postgres host")
@click.option("--pg-port", default=5432, show_default=True, type=int, help="Postgres port")
@click.option("--pg-db", default="ny_taxi", show_default=True, help="Postgres database name")
@click.option("--year", default=2021, show_default=True, type=int, help="Year for taxi data")
@click.option("--month", default=1, show_default=True, type=int, help="Month for taxi data")
@click.option("--table-name", default="yellow_taxi_data", show_default=True, help="Destination table name")
@click.option("--chunk-size", default=100000, show_default=True, type=int, help="CSV chunk size for ingestion")
@click.option("--url", default=None, help="Override source CSV URL")
def run(pg_user, pg_password, pg_host, pg_port, pg_db, year, month, table_name, chunk_size, url):
    if url is None:
        prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow'
        url = f'{prefix}/yellow_tripdata_{year}-{month:02d}.csv.gz'

    engine = create_engine(
        f'postgresql+psycopg://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}'
    )

    if url.endswith('.parquet'):
        print("Reading local parquet file...")
        df = pd.read_parquet(url)
        df_iter = [df]
    else:
        df_iter = pd.read_csv(url, iterator=True, chunksize=100000)

    first = True

    for df_chunk in tqdm(df_iter):
        for col in possible_dates:
            if col in df_chunk.columns:
                df_chunk[col] = pd.to_datetime(df_chunk[col])
        if first:
            print('creating table')
            df_chunk.head(n=0).to_sql(
                name=table_name,
                con=engine,
                if_exists='replace',
            )
            first = False

        df_chunk.to_sql(
            name=table_name,
            con=engine,
            if_exists='append',
        )


if __name__ == '__main__':
    run()








