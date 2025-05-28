from django.shortcuts import render, redirect
from django.views.debug import technical_404_response

from .forms import EventForm
from .models import EventRegistration
def index(request):
    return render(request, 'webtechapp/index.html')


def events2_view(request):
    return render(request, 'webtechapp/eve.html')  # adjust if needed
def register(request):
    table=EventRegistration()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        payment=request.POST.get('paymentMethod')
        category = request.POST.get('categorySelect')
        event = request.POST.get('event')
        total_amount = int(request.POST.get("totalAmount", 0))

        # databse tables

        table.name=name
        table.email=email
        table.phone=phone
        table.payment_method=payment
        table.event_name = event
        table.event_category = category
        table.event_price = total_amount
        table.save()

        return redirect('index')
    return render(request, 'webtechapp/Reg.html')

def view_registrations(request):
    all_data = EventRegistration.objects.all()
    return render(request, 'webtechapp/viewreg.html', {'data': all_data})

