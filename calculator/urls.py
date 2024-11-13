from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_input_view,name='user_input'),
    path('process_results/',views.process_results,name='process_results'),
]
