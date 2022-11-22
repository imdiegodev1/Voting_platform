from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    #Ex: /polls/
    path("", views.IndexView.as_view(), name="index"),  ##Based on classes
    #Ex: /polls/5
    ##path("<int:question_id>/", views.detail, name="detail"),
    path("<int:pk>/detail", views.DetailView.as_view(), name="detail"),
    #Ex: /polls/5/results
    ##path("<int:question_id>/results>", views.results, name="results"),
    path("<int:pk>/results>", views.ResultsView.as_view(), name="results"),
    #Ex: /polls/5/votes
    path("<int:question_id>/votes>", views.vote, name="vote"),
    #Ex: /about
    path("about", views.About.as_view(), name="about")
]