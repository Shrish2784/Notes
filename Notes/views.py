from django.shortcuts import render
from Notes import forms
from Notes import models
# Create your views here.
def index(request):
    form = forms.Note_form
    note = models.Note.objects.all()
    context_dict = {
        'form':form,
        'note':note,
    }
    if request.method == 'POST':
        form = forms.Note_form(request.POST)
        if form.is_valid():
            form.save(commit=True)

    return render(request, "Notes/index.html", context=context_dict)