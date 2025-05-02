from django.shortcuts import render

def index(request):
    return render(request, 'webtechapp/index.html')


def events2_view(request):
    return render(request, 'webtechapp/eve.html')  # adjust if needed
# def register(request):
#     if request.method == 'POST':
#         # process form data
#         return render(request, 'success.html')  # or redirect
#     return render(request, 'register.html')