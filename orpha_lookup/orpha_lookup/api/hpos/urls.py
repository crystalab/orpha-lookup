from django.urls import path

from orpha_lookup.api.hpos.views import HpoViewSet

app_name = 'hpos'

urlpatterns = [
    path('', HpoViewSet.as_view({'get': 'list'}), name='suggest')
]
