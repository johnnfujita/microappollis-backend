from django.urls import path
from . import views

app_name = 'ggg_art'

urlpatterns = [
    
    path('art-categories/', views.ArtCategoryList.as_view(), name='art-category-list'),
    path('art-categories/<pk>/', views.ArtCategoryDetail.as_view(), name='art-category-detail'),
    path('techniques/', views.TechniqueList.as_view(), name='technique-list'),
    path('techniques/<pk>/', views.TechniqueDetail.as_view(), name='technique-detail'),
    path('artworks/', views.ArtworkList.as_view(), name='artwork-list'),
    path('artworks/<pk>/', views.ArtworkDetail.as_view(), name='artwork-detail'),
    path('printed-artworks/', views.PrintedArtworkList.as_view(), name='printed-artwork-list'),
    path('printed-artworks/<pk>/', views.PrintedArtworkDetail.as_view(), name='printed-artwork-detail'),
    path('limited-artworks/', views.LimitedArtworkList.as_view(), name='limited-artwork-list'),
    path('limited-artworks/<pk>/', views.LimitedArtworkDetail.as_view(), name='limited-artwork-detail'),
    path('artists/', views.ArtistList.as_view(), name='artist-list'),
    path('artists/<pk>/', views.ArtistDetail.as_view(), name='artist-detail'),
    path('locations/', views.LocationList.as_view(), name='location-list'),
    path('locations/<pk>/', views.LocationDetail.as_view(), name='location-detail'),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name)
    
]
