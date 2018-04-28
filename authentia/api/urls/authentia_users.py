from django.urls import path

from users.views import authentia_users as views

urlpatterns = [
    path('', views.AuthentiaListCreateView.as_view()),
    path('<int:pk>/', views.AuthentiaUserRetrieveUpdateDestroyView.as_view()),
    path('auth/', views.AuthentiaUserAuthView.as_view()),
]
