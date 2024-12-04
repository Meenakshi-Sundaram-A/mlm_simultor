from django.urls import path
from . import views

urlpatterns = [
    #path('',views.user_input_view,name='user_input_view'),
    path('',views.binarylevel_input_view,name='binarylevel_input'),
    path('unilevel/',views.unilevel_input_view,name='unilevel_input'),
    path('matrixlevel/',views.matrixlevel_input_view,name='matrixlevel_input'),
    path('process_results/',views.process_results,name='process_results'),
]
