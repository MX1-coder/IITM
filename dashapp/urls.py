# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from dashapp import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
     re_path(r'^.*\.*', views.pages, name='pages'),
    
    # path('userprofile/', views.userprofile, name='userprofile'),
    # path('typography/', views.typography, name='typography'),
    # path('tablelist/', views.tablelist, name='tablelist'),
    # path('', views.index, name='home'),
    # path('', views.index, name='home'),

]
