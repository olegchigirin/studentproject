from django.shortcuts import render


def home(request):
    return render(request, 'experiment/experiment/experiment_home.html')