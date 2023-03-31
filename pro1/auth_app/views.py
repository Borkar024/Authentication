from  rest_framework.generics import CreateAPIView
from .serializers import UserSerializers

class UserAPI(CreateAPIView):
    serializer_class = UserSerializers
    