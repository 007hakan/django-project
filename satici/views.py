from django.shortcuts import render,redirect,get_object_or_404
from .models import Satici
from django.contrib import messages
from .forms import SaticiForm

# Create your views here.
def index(request):
    saticis=Satici.objects.all()
    context= {
        "saticis" : saticis
    }
    return render(request,"index.html",context)
def urunler(request,satici_id):
    satici = Satici.objects.filter(id=satici_id)
    context = {
        "satici":satici
    }

    return render(request,'urunler.html',context)

def urun_ekle(request):
    if request.method == "POST":
        header = request.POST.get('header')
        text = request.POST.get('text')
        
        satici = Satici(header=header,text=text)
        satici.save()
        messages.success(request,'Successfully Added.')

        return redirect("/")
    return render(request,"urun_ekle.html")

def urun_sil(request,satici_id):
    satici = get_object_or_404(Satici,id=satici_id)
    if request.method == 'POST':
        satici.delete() 
        messages.success(request,'Successfully Deleted.')
        return redirect('/')
    return render(request, 'index.html', {'satici': satici})
def urun_guncelle(request,satici_id):
    
    satici = get_object_or_404(Satici,id=satici_id)
    form = SaticiForm(request.POST or None,request.FILES or None,instance = satici)

    if form.is_valid():
        satici=form.save(commit=False)
        satici.user=request.user
        satici.save()
        messages.success(request,'Update Successfull')
        return redirect('urunler.html')
    return render(request,'index.html',{'form':form})
def about(request):
    return render(request,"about.html")