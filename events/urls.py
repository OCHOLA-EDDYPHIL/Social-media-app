from django.urls import path
from . import views
# from authentication import urls

urlpatterns = [
    path('home', views.home, name='home'),
    path('ticket', views.ticket, name='ticket'),
    # path('logout_view', )
]