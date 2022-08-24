
from . import views
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import TaskCreateView,TaskUpdateView,TaskDeleteView


urlpatterns=[
    path('', views.welcome, name='welcome'),
    path('index/',views.index,name = 'index'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('task/new/', TaskCreateView.as_view(), name='task-create'),
    path('task/<int:pk>/update/',TaskUpdateView.as_view(), name="task-update"),
    path('task/<int:pk>/delete/',TaskDeleteView.as_view(), name="task-delete"),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)