app_name='nothing'
from django.urls import path
from app2.views import*
urlpatterns=[
    path('ntr/',ntr,name=''),
]