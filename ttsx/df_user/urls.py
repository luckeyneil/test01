from django.conf.urls import url

from df_user import views

urlpatterns = [
    url(r'^index3', views.index3),
    url(r'^index2', views.index2),
]