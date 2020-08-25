from django.urls import path, include
from djoser import views as djoser_views
urlpatterns = [
    # Views are defined in Djoser, but we're assigning custom paths.
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),  
]