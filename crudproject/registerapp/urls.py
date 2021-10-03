from django.urls import path
from .views import RegisterView, UserDetail

urlpatterns = [
    path('', RegisterView.as_view()),
    path('<int:pk>/', UserDetail.as_view())
]