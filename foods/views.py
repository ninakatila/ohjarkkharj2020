from django.shortcuts import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.TemplateView):
    template_name= 'foods/index.html'


class QuestionView(generic.ListView):
    template_name = 'foods/question.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):

	    return Question.objects.filter(
	        pub_date__lte=timezone.now()
	    ).order_by('pub_date')

class DetailView(generic.DetailView):
    model = Question
    template_name = 'foods/detail.html'
    def get_queryset(self):

        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'foods/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'foods/detail.html', {
            'question': question,
            'error_message': "Et valinnut ruokaa vielä",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('foods:results', args=(question.id,)))

class QuitView(generic.TemplateView):
    template_name= 'foods/quit.html'
