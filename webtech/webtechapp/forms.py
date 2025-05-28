from django import forms

# Static category/event/price choices (you can customize this)
CATEGORIES = {
    'Indoor': [('Chess', 50), ('Carrom', 60)],
    'Outdoor': [('Football', 100), ('Cricket', 120)],
}

EVENT_CHOICES = [
    (f"{cat}-{name}-{price}", f"{name} ({cat}) - ₹{price}")
    for cat, events in CATEGORIES.items()
    for name, price in events
]

class EventForm(forms.Form):
    name = forms.CharField(label="Name")
    email = forms.EmailField(label="Email")
    phone = forms.CharField(label="Phone")
    payment_method = forms.ChoiceField(choices=[
        ('Online', 'Online'),
        ('Offline', 'Offline')
    ])
    selected_events = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=EVENT_CHOICES,
        label="Select Events"
    )
