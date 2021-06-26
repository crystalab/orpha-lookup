from django.urls import path

from orpha_lookup.api.disorders.views import DisorderViewSet

app_name = 'disorders'

urlpatterns = [
    path('', DisorderViewSet.as_view({'get': 'list'}), name='list')
]
