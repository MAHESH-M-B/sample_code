from django.urls import path, include

from form import views

urlpatterns = [
    path('form/', views.form, name='form'),
    path('formview/', views.form_view, name='form_view'),
]