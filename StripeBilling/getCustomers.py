from workspace.StripeBilling.page1 import State
import pandas as pd
import stripe


def getCustomers(state: State) -> pd.DataFrame:
    stripe.api_key = "your_api_key"
    customers = stripe.Customer.list(limit=5).get("data")
    customers_dataframe = pd.DataFrame(customers)
    return customers_dataframe[["id", "email", "name"]]
