from django.conf.urls import url
from . import views

from django.conf import settings
from django.conf.urls.static import static
from .views import TaskCreateView


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^register/', views.registerPage, name="register"),
    url(r'^login/', views.loginPage, name="login"),
    url(r'^logout/', views.logoutUser, name="logout"),
    url(r'^task/new/', TaskCreateView.as_view(), name='task-create'),    

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)