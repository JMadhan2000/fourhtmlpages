from django.shortcuts import render

# Create your views here.
def movie1(request):
    return render(request,'arjunreddy.html')

def movie2(request):
    return render(request,'leo.html')


def movie3(request):
    return render(request,'mad.html')


def movie4(request):
    return render(request,'japan.html')