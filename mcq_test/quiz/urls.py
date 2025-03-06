from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('test/<int:test_id>/question/<int:question_number>/', views.start_test, name='start_test'),
    path('test/<int:test_id>/submit_answer/<int:question_number>/', views.submit_answer, name='submit_answer'),
    path('test/<int:test_id>/summary/', views.test_summary, name='test_summary'),
]