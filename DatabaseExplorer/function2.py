from workspace.DatabaseExplorer.page1 import State
import pandas as pd

import os
import psycopg2

conn_params = {
    "dbname": os.environ["SOURCE_PG_DROPBASEDEMODB_DATABASE"],
    "user": os.environ["SOURCE_PG_DROPBASEDEMODB_USERNAME"],
    "password": os.environ["SOURCE_PG_DROPBASEDEMODB_PASSWORD"],
    "host": os.environ["SOURCE_PG_DROPBASEDEMODB_HOST"],
    "port": os.environ["SOURCE_PG_DROPBASEDEMODB_PORT"],
}


def fetch_query(query, conn_params):
    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchall()
            colnames = [desc[0] for desc in cur.description]

    return pd.DataFrame(result, columns=colnames)


def function2(state: State) -> pd.DataFrame:
    query = state.widgets.widget1.input2

    return fetch_query(query, conn_params)
