from django.urls import path
from myapp import views
urlpatterns = [
    
    path("Registrations/",views.Registrations.as_view()),
    path("Registrations/<int:idd>/",views.Registrations.as_view())
]
