from workspace.Feat.page1 import Context, State
from sqlalchemy import create_engine
import os

SOURCE_PG_DROPBASEDEV_HOST = os.environ.get("SOURCE_PG_DROPBASEDEV_HOST")
SOURCE_PG_DROPBASEDEV_USERNAME = os.environ.get("SOURCE_PG_DROPBASEDEV_USERNAME")
SOURCE_PG_DROPBASEDEV_PASSWORD = os.environ.get("SOURCE_PG_DROPBASEDEV_PASSWORD")
SOURCE_PG_DROPBASEDEV_PORT = os.environ.get("SOURCE_PG_DROPBASEDEV_PORT")
SOURCE_PG_DROPBASEDEV_DATABASE = os.environ.get("SOURCE_PG_DROPBASEDEV_DATABASE")

DEMO_DATABASE_URL = f"postgresql+psycopg2://{SOURCE_PG_DROPBASEDEV_USERNAME}:{SOURCE_PG_DROPBASEDEV_PASSWORD}@{SOURCE_PG_DROPBASEDEV_HOST}:{SOURCE_PG_DROPBASEDEV_PORT}/{SOURCE_PG_DROPBASEDEV_DATABASE}"


def createFeature(state: State, context: Context) -> Context:
    engine = create_engine(DEMO_DATABASE_URL)
    connection = engine.connect()
    response = connection.execute(
        f"INSERT INTO feature (name, description, is_enabled) VALUES ('{state.widgets.featureCreator.input1}', '{state.widgets.featureCreator.input2}', '{state.widgets.featureCreator.select1}')"
    )
    if response.rowcount > 0:
        context.widgets.featureCreator.message = f"Successfully created feature!"
        context.widgets.featureCreator.message_type = "success"
    else:
        context.widgets.featureCreator.message = "Unable to create feature!"
        context.widgets.featureCreator.message_type = "error"

    return context
