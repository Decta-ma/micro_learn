# from django.shortcuts import render
from django.views.generic import TemplateView
# from django.views.decorators.csrf import csrf_protect

# @csrf_protect
# def my_view(request):
#     if request.method == 'POST':
#         # Handle form submission
#         pass



class HomeView(TemplateView):
    template_name='home.html'
    
