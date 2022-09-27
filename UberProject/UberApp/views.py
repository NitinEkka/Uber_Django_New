from django.shortcuts import render
from .models import Uber

def price(request):
     if request.method=="POST":
           DBP = int(request.POST.get("DBP"))
           DAP = int(request.POST.get("DAP"))
           TMF = int(request.POST.get("TMF"))
           Distance = int(request.POST.get("Distance"))


           Total_Price = (DBP + (Distance*DAP))*TMF
           nw = Uber(DBP=DBP, DAP=DAP, TMF=TMF, Distance=Distance)
           nw.save()
           print('Invoice Created')
           
           return render(request,'invoice.html',{"TP":Total_Price})




     return render(request,'form.html')



