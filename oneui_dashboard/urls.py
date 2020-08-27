
from oneui_dashboard import views
from django.conf.urls import url, include


urlpatterns = [
    url(r'', views.home, name='home'),
    url(r'oneui_dashboard/', views.home, name='home')
    
]