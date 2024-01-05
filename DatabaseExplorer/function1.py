from workspace.DatabaseExplorer.page1 import Context, State

import os
from openai import OpenAI


def generate_sql(query):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"Generate a SQL query that gets the following data. The available databases are users and orders. Data to get: {query}. Only respond with the SQL query, nothing else.",
            }
        ],
        model="gpt-3.5-turbo",
    )

    return chat_completion.choices[0].message.content


def function1(state: State, context: Context) -> Context:
    query = state.widgets.widget1.input1

    sql = generate_sql(query)

    context.widgets.widget1.message = sql
    return context
