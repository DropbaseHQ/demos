from workspace.StripeBilling.page1 import State
import pandas as pd
import stripe


def getCustomerDetails(state: State) -> pd.DataFrame:
    stripe.api_key = "your_api_key"
    customer_data = stripe.Customer.retrieve(state.tables.customers.id)
    df = pd.DataFrame([customer_data])
    return df
