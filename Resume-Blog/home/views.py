from django.shortcuts import render

def resume(request):
    print("hiiiiii")
    return render(request, "indexr.html")
