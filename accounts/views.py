from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# Create your views here.



class SignUpView(generic.CreateView):
    form_class = UserCreationForm
#reverse_lazy usage is due to URLs of the generic class-based views
#are not loaded when the file is imported
    success_url = reverse_lazy('login')
    template_name = 'signup.html'