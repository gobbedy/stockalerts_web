from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reddit/', views.reddit, name='reddit'),
    path('test/', views.test, name='test'),
    path('<path:basename>/', views.catch, name='catch')
    #path('movers/',views.movers, name='dashboard-movers'),
    #path('yahoo_movers/', views.max_gainer, name='dashboard-movers'),
    #path('<str:ticker>/', views.get_details_ticker, name='dashboard-ticker'),
]