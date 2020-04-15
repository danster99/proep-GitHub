from rest_framework.viewsets import ModelViewSet
from api.users.models import User
from api.users.serializers import UserSerializer


class UserList(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        """
        Retrieve existing clients. It is possible to filter clients by email.
        ex: ?email='some-client@mail.com'
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve existing clients. It is possible to filter clients by email.
        ex: ?email='some-client@mail.com'
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().retrieve(request, *args, **kwargs)

    # def get(self, format=None):
    #     houses = User.objects.all
    #     serializer = UserSerializer(houses)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
