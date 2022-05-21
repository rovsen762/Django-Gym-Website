
from django.shortcuts import render
from django.urls import reverse_lazy
from blogs.models import Blog
from django.views.generic.edit import FormView
from . forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = "We received your request"

    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

def index(request):
    last_blogs = Blog.objects.order_by('-date')[:3]
    context = {
        'last_blogs':last_blogs
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')