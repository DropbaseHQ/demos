from workspace.Feat.page1 import Context, State
from sqlalchemy import create_engine
import os

SOURCE_PG_DROPBASEDEV_HOST = os.environ.get("SOURCE_PG_DROPBASEDEV_HOST")
SOURCE_PG_DROPBASEDEV_USERNAME = os.environ.get("SOURCE_PG_DROPBASEDEV_USERNAME")
SOURCE_PG_DROPBASEDEV_PASSWORD = os.environ.get("SOURCE_PG_DROPBASEDEV_PASSWORD")
SOURCE_PG_DROPBASEDEV_PORT = os.environ.get("SOURCE_PG_DROPBASEDEV_PORT")
SOURCE_PG_DROPBASEDEV_DATABASE = os.environ.get("SOURCE_PG_DROPBASEDEV_DATABASE")

DEMO_DATABASE_URL = f"postgresql+psycopg2://{SOURCE_PG_DROPBASEDEV_USERNAME}:{SOURCE_PG_DROPBASEDEV_PASSWORD}@{SOURCE_PG_DROPBASEDEV_HOST}:{SOURCE_PG_DROPBASEDEV_PORT}/{SOURCE_PG_DROPBASEDEV_DATABASE}"


def disableFeat(state: State, context: Context) -> Context:
    engine = create_engine(DEMO_DATABASE_URL)
    connection = engine.connect()
    response = connection.execute(
        f"UPDATE feature SET is_enabled = false WHERE id = {state.tables.features.id}"
    )
    if response.rowcount > 0:
        context.widgets.featureController.message = f"Successfully disabled feature!"
        context.widgets.featureController.message_type = "success"
    else:
        context.widgets.featureController.message = "Unable to disable feature!"
        context.widgets.featureController.message_type = "error"
    return context
