from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='hi how r u '
    d={'access':data}
    return render(request,'data_render.html',context=d)

