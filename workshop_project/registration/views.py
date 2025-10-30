from django.shortcuts import render
from django.core.mail import send_mail
from .forms import WorkshopForm

def register_workshop(request):
    if request.method == 'POST':
        form = WorkshopForm(request.POST)
        if form.is_valid():
            form.save()

            # Send success email
            subject = 'Workshop Registration Successful'
            message = 'Thank you for registering for the workshop!'
            recipient = form.cleaned_data['email']

            send_mail(subject, message, 'admin@example.com', [recipient])

            return render(request, 'success.html', {'name': form.cleaned_data['name']})
    else:
        form = WorkshopForm()

    return render(request, 'register.html', {'form': form})
