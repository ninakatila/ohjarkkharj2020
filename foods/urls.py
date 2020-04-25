from django.urls import path

from . import views

app_name = 'foods'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('question/', views.QuestionView.as_view(), name='question'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('quit/', views.QuitView.as_view(), name='quit'),
]
