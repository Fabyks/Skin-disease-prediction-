from django.urls import path
from . import views
urlpatterns = [
    path('skin_disease_prediction/',views.skin_disease_prediction,name='skin_disease_prediction'),
    path('get_skin_disease_prediction/',views.get_skin_disease_prediction,name='get_skin_disease_prediction'),
    path('view_doctors/',views.view_doctors,name='view_doctors'),
    path('appoint_doctor',views.appoint_doctor,name='appoint_doctor'),
    path('view_appointments',views.view_appointments,name='view_appointments'),
]
