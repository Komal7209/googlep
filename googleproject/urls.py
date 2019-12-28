from django.conf.urls import url
from googleproject import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
]