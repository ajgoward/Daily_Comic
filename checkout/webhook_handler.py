from django.http import HttpResponse


class StripeWH_Handler:
    """handle stripe web hooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):

        """handle a generic webhook"""

        return HttpResponse(
            content=f'webhook recieved: {event["type"]}',
            status=200
        )
