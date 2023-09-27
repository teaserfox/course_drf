from django.urls import path
from app_spa.apps import AppSpaConfig

from app_spa.views import HabitListAPIView, PublicHabitListAPIView, HabitCreateAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = AppSpaConfig.name

urlpatterns = [
    path('habits/', HabitListAPIView.as_view(), name='habit_list'),
    path('habits/public/', PublicHabitListAPIView.as_view(), name='public_habit_list'),
    path('habits/create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('habits/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('habits/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='delete'),
]