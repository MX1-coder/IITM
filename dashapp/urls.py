# -*- encoding: utf-8 -*-

from django.urls import path, re_path
from dashapp import views
from dashboard.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [

    # The home page
    path('', views.index, name='index'),
    path('category/', views.categoryshow, name='categoryshow'),
    path('table/', views.tablelist, name='tablelist'),
    path('typography/', views.typography, name='typography'),
    path('notifications/', views.notifiactions, name='notifications'),
    path('userprofile/', views.userprofile, name='userprofile'),

     #product urls
    path('createproduct/', views.createproduct, name='createproduct'),
    path('showproduct/', views.showproduct, name='showproduct'),
    path('editproduct/', views.editproduct, name='editproduct'),
    path('update/<int:id>', views.update_product),
    path('delete/<int:id>', views.delete_product),
   
    


    #Employee urls

    path('createemployee/', views.createemployee, name='createemployee'),
    path('showemployee/', views.showemployee, name='showemployee'),
    path('editemployee/', views.editemployee, name='editemployee'),
    path('update1/<int:id>', views.update_employee),
    path('delete1/<int:id>', views.delete_employee),

#------------order urls
    path('createorder/', views.createorder, name='createorder'),
    path('showorder/', views.showorder, name='showorder'),
    path('editorder/', views.editorder, name='editorder'),
    path('update2/<int:id>', views.update_order),
    path('delete2/<int:id>', views.delete_order),




    # Matches any html file
    #  re_path(r'^.*\.*', views.pages, name='pages'),
    # re_path(r'^orders/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.OrderView.as_view(), name='orders'),

]
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)