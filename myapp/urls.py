"""Early_warning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('forest_division/',views.forest_division),
    path('view_forest_division/',views.view_forest_division),
    path('edit_forest_division/<str:did>',views.edit_forest_division),
    path('station/',views.station),
    path('view_station/',views.view_station),
    path('animal/',views.animal),
    path('view_animal/',views.view_animal),
    path('edit_animal/<did>',views.edit_animal),
    path('reserved/<did>',views.reserved),
    path('forest_officer/',views.forest_officer),
    path('forest_officer_post/',views.forest_offecer_post),
    path('view_officer/',views.view_officer),
    path('edit_officer/<did>',views.edit_officer),
    path('view_usercomplaint/',views.view_usercomplaint),
    path('view_usercomplaint_search/',views.view_usercomplaint_search),
    path('send_reply/<did>',views.send_reply),
    path('send_reply_post/',views.send_reply_post),
    path('notification/<did>',views.notification),
    path('notification_v/',views.notification_view),
    # path('allocation/',views.allocation),
    # path('view_allocation/',views.view_allocation),
    # path('edit_allocation/',views.edit_allocation),
    path('admin_home/',views.admin_home),
    path('admin_view_detections/',views.admin_view_detections),
    path('logout/',views.logout),
    path('contact/',views.contact),
    path('contact_post/',views.contact_post),

    path('forest_division_post/',views.forest_division_post),
    path('delete_division/<str:did>',views.delete_division),
    path('edit_forest_division_post/',views.edit_forest_division_post),
    path('station_post/',views.station_post),
    path('delete_station/<str:did>',views.delete_station),
    path('edit_station/<str:did>',views.edit_station),
    path('edit_station_post/',views.edit_station_post),
    path('notification_post/',views.notification_post),
    path('search_station/',views.search_station),
    path('search_division/',views.search_division),
    path('animal_post/',views.animal_post),
    path('edit_animal_post/',views.edit_animal_post),
    path('delete_animal/<did>',views.delete_animal),
    path('view_receved/',views.view_receved),
    path('search_animal/',views.search_animal),
    path('search_reseved/',views.search_reseved),
    path('delete_officer/<did>',views.delete_officer),
    path('edit_officer_post/',views.edit_officer_post),
    path('search_officer/',views.search_officer),
    path('notification_search/', views.search_notification),
    path('category/', views.category),
    path('category_post/', views.category_post),
    path('view_category/', views.view_category),
    path('search_category/', views.search_category),
    path('delete_category/<did>', views.delete_category),
    path('edit_category/<did>', views.edit_category),
    path('edit_category_post/', views.edit_category_post),

    ##          officer
    path('ohome/', views.ohome),
    path('view_complaint/', views.view_complaint),
    path('view_complaint_search/', views.view_complaint_search),
    path('forward/<id>', views.forward),
    path('alert/', views.alert),
    path('alert_post/', views.alert_post),
    path('view_alert/', views.view_alert),
    path('view_alert_search/', views.view_alert_search),
    path('delete_alert/<id>', views.delete_alert),
    path('view_notification/', views.view_notification),
    path('search_notification_view/', views.search_notification_view),
    path('officer_view_detections/', views.officer_view_detections),

    #######             android
    path('User_Registration', views.User_Registration),
    path('and_login', views.and_login),
    path('and_profile', views.and_profile),
    path('and_update_profile', views.and_update_profile),
    path('Search_Animals', views.Search_Animals),
    path('and_contact', views.and_contact),
    path('and_view_reply', views.and_view_reply),
    path('and_del_comp', views.and_del_comp),
    path('and_send_complaint', views.and_send_complaint),
    path('and_view_alerts', views.and_view_alerts),
    path('and_view_divisions', views.and_view_divisions),
    path('and_view_stations', views.and_view_stations),
    path('and_view_detections', views.and_view_detections),
    path('getallnots', views.getallnots),

]
