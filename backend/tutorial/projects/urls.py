from django.urls import path
from projects import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)