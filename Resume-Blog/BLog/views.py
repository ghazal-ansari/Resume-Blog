from django.shortcuts import render

def index(request):
    return render(request, 'indexb.html')

def post_1(request):
    return render(request, 'post_1.html')

def post_2(request):
    return render(request, 'post_2.html')

def post_3(request):
    return render(request, 'post_3.html')

def post_4(request):
    return render(request, 'post_4.html')

def contact(request):
    return render(request, 'contact.html')

def resume(request):
    return render(request, 'indexr.html')