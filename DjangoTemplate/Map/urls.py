from django.conf.urls import url
from django.urls import path

from Map import views

urlpatterns = [
    url(r'^showmarker/', views.showmarker, name='showmarker'),
    url(r'^ajax_add/', views.ajax_add),

]
