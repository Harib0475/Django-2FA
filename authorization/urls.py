from django.urls import path

from . import views


urlpatterns = [
    path('',views.Profile.as_view(),name='index'),
    path('signup/', views.signup),
    path('logout/',views.logout_,name='logout'),

    path('my_view/',views.my_view,name='my_view')
]
