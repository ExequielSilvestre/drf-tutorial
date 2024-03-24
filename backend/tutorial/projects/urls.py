from django.urls import path
from projects import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('projects/', views.project_list),
    path('projects/<int:pk>/', views.project_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)