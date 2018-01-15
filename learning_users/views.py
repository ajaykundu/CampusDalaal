from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'products': reverse('productapp:product-list', request=request, format=format),
        'messages': reverse('django_private_chat:message_list', request=request, format=format),
        'user': reverse('basic_app:user_list', request=request, format=format),
        'userinfo': reverse('basic_app:userinfo_list', request=request, format=format)
    })
