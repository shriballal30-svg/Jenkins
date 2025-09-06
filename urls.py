from django.urls import path
from employe.views import *
urlpatterns = [
    path('', home),
    path('about/',about),
    path('ragistration/',ragistration),
    path('record/',record),
    path('update/<id>/',update),
    path('delete/<id>/',delete),

]