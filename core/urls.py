from django.urls import path
from . import views 
from .views import SearchResultsView
app_name = 'core' 
urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', views.home, name='home')
]