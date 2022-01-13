from rest_framework import viewsets, status
from django.db.models import F, DecimalField
from django_filters import rest_framework as filters
from rest_framework.response import Response

from .filters import ItemFilter
from .serializers import StaticSerializer
from .models import StaticItem
from .utils import Round


class StaticViewSetApi(viewsets.ModelViewSet):
    """
    View, create and delete statistics
    """
    serializer_class = StaticSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ItemFilter

    def get_queryset(self):
        qs = StaticItem.objects.annotate(cpc=Round(F('cost') / F('click'), output_field=DecimalField()),
                                         cpm=Round(F('cost') / F('views') * 1000, output_field=DecimalField()))
        return qs

    def destroy(self, request, *args, **kwargs):
        StaticItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

