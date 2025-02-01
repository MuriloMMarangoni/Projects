from django.shortcuts import render

import datetime
# Create your views here.
context = {
    'data': datetime.date.today()
}
def home(request):
    return render(request,'home.html',context)