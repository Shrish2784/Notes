from django import forms
from .models import Note
import datetime

class Note_form(forms.ModelForm):
    Title = forms.CharField(label='Title', widget=forms.widgets.TextInput(attrs={
        'id':'title_input',
        'type':'text',
        'placeholder':'Enter the Title.'
    }))

    Data = forms.CharField(label='Note', widget=forms.Textarea(attrs={
        'placeholder':'Enter your note here',
        'id':'note_input',
        'type':'textarea',
        'rows':10,
        'cols':40
    }))
    Date = forms.DateField(label='Date', widget=forms.widgets.DateInput(attrs={
        'type':'date',
        'id':'date_input',
    }), initial=datetime.date.today(),)


    class Meta:
        model = Note
        fields = '__all__'