from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()
def root_route(request):
    return Response({
        "message": "One Ring to rule them all, One ring to find them; One ring to bring them all and in the darkness bind them."
    })
