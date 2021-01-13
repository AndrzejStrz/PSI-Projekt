
from django.urls import path
from . import views
from rest_framework import generics


urlpatterns = [
    path('', views.index, name='index'),

    path('Uzytkownik/', views.UserList.as_view()),
    path('Uzytkownik/<int:pk>/', views.UserDetail.as_view()),

    path('Opcje_Biletu/', views.Ticket_OptionsList.as_view()),
    path('Opcje_Biletu/<int:pk>/', views.Ticket_OptionsDetail.as_view()),

    path('Podroze/', views.TravelList.as_view()),
    path('Podroze/<int:pk>/', views.TravelDetail.as_view()),

    path('Pociag/', views.TrainList.as_view()),
    path('Pociag/<int:pk>/', views.TrainDetail.as_view()),

    path('Wagon/', views.CarriageList.as_view()),
    path('Wagon/<int:pk>/', views.CarriageDetail.as_view()),

    path('Miejsce/', views.SeatsList.as_view()),
    path('Miejsce/<int:pk>/', views.SeatsDetail.as_view()),

    path('Bilet/', views.TicketList.as_view()),
    path('Bilet/<int:pk>/', views.TicketDetail.as_view()),




]
