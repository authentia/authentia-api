from django.urls import path

from users.views import document_types as views

urlpatterns = [
    path('', views.DocumentTypeListCreateView.as_view()),
    path('<int:pk>/', views.DocumentTypeRetrieveUpdateDestroyView.as_view()),
]
