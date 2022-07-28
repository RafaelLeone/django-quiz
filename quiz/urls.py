from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='quiz.index'),
    path('form', views.quiz_form, name='quiz.form'),
]
