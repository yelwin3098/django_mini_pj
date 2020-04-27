from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="doctor-home-page"),
    path('doc/show/all',views.showDoctors,name="doctor-show-page"),
     path('doc/show/<int:pk>',views.filterDoctors,name="doctor-filter-page"),
    path('doc/create',views.createDoctor,name="doctor-crate-page"),
    path('cat/create',views.createCat,name="doctor-cat-create-page")
]