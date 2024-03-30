from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ExpoPushToken
from .serializers import ExpoPushTokenSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

class ExpoPushTokenView(APIView):
    @swagger_auto_schema(
        request_body=ExpoPushTokenSerializer,
        responses={201: 'Created', 400: 'Bad Request'}
    )
    def post(self, request):
        serializer = ExpoPushTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpoPushTokensListView(generics.ListAPIView):
    queryset = ExpoPushToken.objects.all()
    serializer_class = ExpoPushTokenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__id', 'token']

class ExpoPushTokenDetailView(generics.RetrieveAPIView):
    queryset = ExpoPushToken.objects.all()
    serializer_class = ExpoPushTokenSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class ExpoPushTokenDeleteView(generics.DestroyAPIView):
    queryset = ExpoPushToken.objects.all()
    serializer_class = ExpoPushTokenSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class ExpoPushTokenUpdateView(generics.UpdateAPIView):
    queryset = ExpoPushToken.objects.all()
    serializer_class = ExpoPushTokenSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'

class ExpoPushTokenCreateView(generics.CreateAPIView):
    queryset = ExpoPushToken.objects.all()
    serializer_class = ExpoPushTokenSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'id'

