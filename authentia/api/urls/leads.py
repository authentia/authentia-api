from django.urls import path

from users.views import leads as views

urlpatterns = [
    path('', views.LeadListCreateView.as_view()),
    path('<int:pk>/', views.LeadRetrieveUpdateDestroyView.as_view()),
]
