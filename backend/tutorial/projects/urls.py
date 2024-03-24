from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from projects import views

# API endpoints
urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('projects/',
        views.ProjectList.as_view(),
        name='project-list'),
    path('projects/<int:pk>/',
        views.ProjectDetail.as_view(),
        name='project-detail'),
    path('users/',
        views.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])