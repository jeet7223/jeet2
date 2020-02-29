from django.shortcuts import render
from project_app.forms import myform


def index(request):
    dict = {'text':'hello world','number':300}
    return render(request,'index.html',context=dict)

def users(request):
    form = myform()
    if request.method == 'POST':
        form = myform(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("invalid")
    return render(request,'user.html',{'form':form})
