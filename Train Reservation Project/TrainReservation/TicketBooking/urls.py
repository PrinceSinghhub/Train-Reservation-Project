from django.urls import path
from . import views
urlpatterns = [
    
    path('TicketBooking/',views.ticketBook,name='TicketBooking')
]