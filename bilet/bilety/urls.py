from django.urls import path
from . import views

urlpatterns = [

    path('User/', views.UserList.as_view(), name=views.UserList.name),
    path('User/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),

    path('Ticket_Options', views.Ticket_OptionsList.as_view(), name=views.Ticket_OptionsList.name),
    path('Ticket_Options/<int:pk>', views.Ticket_OptionsDetail.as_view(), name=views.Ticket_OptionsDetail.name),

    path('Travel', views.TravelList.as_view(), name=views.TravelList.name),
    path('Travel/<int:pk>', views.TravelDetail.as_view(), name=views.TravelDetail.name),

    path('Train', views.TrainList.as_view(), name=views.TrainList.name),
    path('Train/<int:pk>', views.TrainDetail.as_view(), name=views.TrainDetail.name),

    path('Carriage', views.CarriageList.as_view(), name=views.CarriageList.name),
    path('Carriage/<int:pk>', views.CarriageDetail.as_view(), name=views.CarriageDetail.name),

    path('Seats', views.SeatsList.as_view(), name=views.SeatsList.name),
    path('Seats/<int:pk>', views.SeatsDetail.as_view(), name=views.SeatsDetail.name),

    path('Ticket', views.TicketList.as_view(), name=views.TicketList.name),
    path('Ticket/<int:pk>', views.TicketDetail.as_view(), name=views.TicketDetail.name),

    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
