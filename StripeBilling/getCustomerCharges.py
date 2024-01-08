from workspace.StripeBilling.page1 import State
import pandas as pd
import stripe


def getCustomerCharges(state: State) -> pd.DataFrame:
    stripe.api_key = "your_api_key"
    customer_charges = stripe.Charge.list(
        customer=state.tables.customers.id, limit=5
    ).get("data")
    df = pd.DataFrame(customer_charges)
    return df
