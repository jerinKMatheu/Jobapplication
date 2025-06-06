from django.urls import path
from hr import views
urlpatterns=[
    path('signin',views.loginview.as_view(),name="signin"),
    path('index',views.Dashboard.as_view(),name="index"),
    path('logout',views.Signout.as_view(),name="logout"),
    path('create/',views.Addcategory.as_view(),name="category"),
    path('remove/<int:pk>',views.Categoryremove.as_view(),name="category.del"),
    path('add/',views.Addjob.as_view(),name="addjob"),
    path('deljob',views.Del_job.as_view(),name="remjob"),
    path('jobview/<int:pk>',views.Jobdetails.as_view(),name="jobview"),
    path('joblist/',views.Joblist.as_view(),name="list"),
    path('jobedit/<int:pk>',views.Jobupdate.as_view(),name="edit"),
]