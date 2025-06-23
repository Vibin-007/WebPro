from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import EventRegistration, Student


def index(request):
    if request.method == 'POST':
        name = request.POST.get('reg_name')
        password = request.POST.get('reg_password')

        # Save to Student table
        Student.objects.create(name=name, password=password)
        return HttpResponse("Student registered successfully!")

    return render(request, 'webtechapp/index.html')


def events2_view(request):
    return render(request, 'webtechapp/eve.html')


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        payment_method = request.POST.get('paymentMethod')
        event_category = request.POST.get('categorySelect')
        event_name = request.POST.get('event')
        event_price = request.POST.get("totalAmount")

        try:
            EventRegistration.objects.create(
                name=name,
                email=email,
                phone=phone,
                payment_method=payment_method,
                event_category=event_category,
                event_name=event_name,
                event_price=event_price
            )
            return redirect('index')
        except Exception as e:
            return HttpResponse(f"Error: {e}")

    return render(request, 'webtechapp/Reg.html')


def view_registrations(request):
    all_data = EventRegistration.objects.all().order_by('id')
    return render(request, 'webtechapp/viewreg.html', {'data': all_data})


def edit_registration(request, registration_id):
    registration = get_object_or_404(EventRegistration, id=registration_id)

    if request.method == 'POST':
        try:
            registration.name = request.POST.get('name')
            registration.email = request.POST.get('email')
            registration.phone = request.POST.get('phone')
            registration.save()
            messages.success(request, 'Registration updated successfully!')
            return redirect('viewreg')

        except Exception as e:
            messages.error(request, f'Error updating registration: {e}')

    return render(request, 'webtechapp/edit_reg.html', {'registration': registration})


def delete_registration(request, registration_id):
    registration = get_object_or_404(EventRegistration, id=registration_id)

    if request.method == 'POST':
        try:
            registration.delete()
            messages.success(request, 'Registration deleted successfully!')
        except Exception as e:
            messages.error(request, f'Error deleting registration: {e}')

    return redirect('viewreg')
