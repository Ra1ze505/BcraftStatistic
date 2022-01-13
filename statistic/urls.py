from django.urls import path

from .views import StaticViewSetApi

app_name = 'statistic'

urlpatterns = [
    path('', StaticViewSetApi.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='view-sets')
]
