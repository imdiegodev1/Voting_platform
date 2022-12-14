from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from .models import Question, Choice

#def index(request):
#
#    latest_question_list = Question.objects.all()
#    context = {
#        "latest_question_list": latest_question_list
#    }
#    return render(request, "polls/index.html", context)

class IndexView (generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published question"""

        return Question.objects.order_by("-pub_date")[:5]

#def detail(request, question_id):
#    question = get_object_or_404(Question, pk=question_id)
#
#    context = {
#        "question": question
#    }
#
#    return render(request, "polls/detail.html", context)

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


#def results(request, question_id):
#    
#    question = get_object_or_404(Question, pk=question_id)
#    
#    context = {
#        "question": question
#    }
#
#    return render(request, "polls/results.html", context)

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

class About(TemplateView):
    template_name = "polls/about.html"

def vote(request, question_id):
    
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        context = {
            "question": question,
            "error_message": "No elegiste una respuesta"
        }
        return render(request, "polls/detail.html", context)
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))