from django.urls import path, include
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<pk>/results', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<question_id>/vote', views.vote, name='vote')
]