from django.contrib import messages
# from django.views import View
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.views.decorators.csrf import csrf_protect

@csrf_protect


def thank(request):
    return render(request, 'contact.html')


def IndexView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank You')
            return redirect('index')  # Redirect after successful form submission
        else:
            messages.warning(request, 'Invalid Input')
    else:
        form = ContactForm()  # Display the form on GET request
    
    return render(request, 'index.html', {'form': form})

