from django.shortcuts import render
from django.views.generic import ListView
from . models import Trainer

class TrainersPageView(ListView):
    model = Trainer
    template_name = 'trainers.html'
    

    


