from django.shortcuts import render

def index(request):
    data = {
    'id': 1234,
    'product': "I Phone",
    'description': '128GB storage 16GB RAm'
    }
    return render(request,'index.html',{'myObject': data})