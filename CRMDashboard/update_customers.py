from workspace.crm_dashboard3.page1 import Context, State

import psycopg2
import os

conn_params = {'dbname': os.environ['SOURCE_PG_DROPBASEDEV_DATABASE'],
              'user': os.environ['SOURCE_PG_DROPBASEDEV_USERNAME'],
              'password': os.environ['SOURCE_PG_DROPBASEDEV_PASSWORD'],
              'host': os.environ['SOURCE_PG_DROPBASEDEV_HOST'],
              'port': os.environ['SOURCE_PG_DROPBASEDEV_PORT']}

def update_customers(state: State, context: Context) -> Context:
    selected_type = state.widgets.widget1.customer_types
    selected_customer = state.tables.customers.customer_id

    with psycopg2.connect(**conn_params) as conn:
        with conn.cursor() as cur:
            update_query = "UPDATE customers SET customer_type = %s WHERE customer_id = %s"
            cur.execute(update_query, (selected_type, selected_customer))

    context.widgets.widget1.message = "Updated Customer"
    return context
