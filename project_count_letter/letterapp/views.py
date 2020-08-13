from django.shortcuts import render

# Create your views here.

def w_letter(request):
    return render(request, 'w_letter.html')

def result(request):
    length = len(request.POST['letter'])
    return render(request, 'result.html', {'length':length} )