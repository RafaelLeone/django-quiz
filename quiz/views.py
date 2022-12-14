from django.shortcuts import redirect, render

from quiz.forms import QuizModelForm
from quiz.models import Quiz


# Create your views here.
def index(request):
    quizes = Quiz.objects.all()
    contexto = {
        'quizes': quizes
    }
    return render(request, 'quiz/index.html', contexto)


def quiz_form(request):
    if request.method == 'POST':
        form = QuizModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            contexto = {
                'form': form,
            }
            return render(request, 'quiz/quiz_form.html', contexto, status=400)

    contexto = {
        'form': QuizModelForm()
    }
    return render(request, 'quiz/quiz_form.html', contexto)
