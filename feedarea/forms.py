from django import forms
from feedarea.models import QuestionInput

class QuestionInputForm(forms.ModelForm):
    Question = forms.CharField(widget=forms.Textarea(attrs={'style':'resize:none;','rows': 2, 'cols': 100, 'class':'container border-1 rounded mt-2 w-75','placeholder':"Ask Your Yes/No Question here"  }), label='')
    class Meta:
        model = QuestionInput
        fields = ['Question']