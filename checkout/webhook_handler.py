from django.http import HttpResponse


class StripeWH_Handler:
    """handle stripe web hooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):

        """handle a generic webhook"""

        return HttpResponse(
            content=f' Unhandled webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_success(self, event):

        """handle a payment intent succeed webhook"""
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'webhook recieved: {event["type"]}',
            status=200
        )

    def handle_payment_failed(self, event):

        """handle a payment intent fail webhook"""

        return HttpResponse(
            content=f'webhook recieved: {event["type"]}',
            status=200
        )
