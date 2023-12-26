from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('ticket_reports/',views.ticket_reports,name='ticket_reports'),
    path('ticket_list/',views.ticket_list,name='ticket_list'),
    path('ticket_details/<str:tkt_id>/', views.ticket_details, name='ticket_details'),

    path('accept_ticket/<int:ticket_id>/', views.accept_ticket, name='accept_ticket'),
    path('decline_ticket/<int:ticket_id>/', views.decline_ticket, name='decline_ticket'),
]