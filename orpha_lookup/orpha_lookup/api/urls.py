from django.urls import include, path

app_name = 'api'

urlpatterns = [
    path('disorders/', include('orpha_lookup.api.disorders.urls')),
    path('hpos/', include('orpha_lookup.api.hpos.urls')),
]
