from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from core_app.models import Phone
from core_app.permissions import IsAdminUser
from core_app.serializers import PhoneSerializer, PhoneDetailSerializer


class PhoneView(ModelViewSet):
    queryset = Phone.objects.all().order_by('-id')
    serializer_class = PhoneSerializer
    #permission_classes = (IsAdminUser,)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'color', 'memory']


class PhoneDetailView(ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneDetailSerializer
    #permission_classes = (IsAdminUser, )
    lookup_field = 'pk'

