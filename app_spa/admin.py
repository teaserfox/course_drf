from django.contrib import admin
from app_spa.models import Habit

admin.site.register(Habit)  # регистрация модели "привычка" в админ-панели
