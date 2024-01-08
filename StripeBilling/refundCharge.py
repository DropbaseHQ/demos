from workspace.StripeBilling.page1 import Context, State
import stripe


def refundCharge(state: State, context: Context) -> Context:
    stripe.api_key = "your_api_key"
    response = stripe.Refund.create(charge=state.tables.charges.id)
    refund_id = response.get("id")
    if refund_id:
        context.widgets.chargeRefunder.message = (
            f"Successfully created refund with id: {refund_id}"
        )
        context.widgets.chargeRefunder.message_type = "success"
    else:
        context.widgets.chargeRefunder.message = "Unable to create refund!"
        context.widgets.chargeRefunder.message_type = "error"

    return context
