from django.urls import path
from.views import send_email
urlpatterns = [
    path('enviar/',send_email,name="send")
]
