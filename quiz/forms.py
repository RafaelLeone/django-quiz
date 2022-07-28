from django import forms

from quiz.models import Quiz


class QuizModelForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            "pergunta",
            "descricao",
            "autor",
            "imagem",
        ]
