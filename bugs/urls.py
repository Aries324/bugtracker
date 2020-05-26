from django import path
from bugs import views


urlpatterns = [
    path('', views.index, name='homepage')
]