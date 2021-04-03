from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('<str:eve_name>/<int:action>/',views.update_status,name="update_status"),
    path('',views.logout_view,name="logout_view"),
    # path('<str:event_name>/',views.getRejectedBitch,name="getRejectedBitch"),
    ]