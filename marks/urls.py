from django.urls import path
from . import views

urlpatterns = [
    path('', views.fetch_marks_table, name='fetch_marks'),
]
