from django.shortcuts import render,redirect,reverse
from django.http import HttpResponseRedirect
from .models import UserLogin,Product,LaptopData,MobileData
# Create your views here.
from django.core.files.storage import FileSystemStorage

def RegisterView(request):
    if request.method == "GET":
        return render(request, "crud/register.html", {})
    elif request.method == "POST":
        user = request.POST.get("username")
        password = request.POST.get("password")
        try:
            if user not in UserLogin.objects.all():
                UserLogin.objects.create(username=user, password=password)
                return redirect(login_view)
        except Exception:
            return redirect(RegisterView)
    return render(request, "crud/register.html", {})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'crud/login.html', context={"messages": "Details Received"})
    elif request.method == 'POST':
        s = UserLogin.objects.filter(username=request.POST.get("username"), password=request.POST.get("password"))
        if s:
            request.session["username"] = request.POST.get("username")
            return redirect(homeview)
        else:
            return redirect(RegisterView)


def homeview(request):
    if request.session.has_key("username"):
        if request.method == "GET":
            return render(request,"crud/home.html",{})
        elif request.method == "POST":

            name_of_product = request.POST.get("name")
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            description = request.POST.get("description")
            u = Product()
            u.name = name_of_product
            u.image = uploaded_file_url
            u.description=description
            type = request.POST.get("typeofproduct")
            u.type =type
            u.save()
            if u.type == "mobile":
                processor = request.POST.get("processormobile")
                ram = request.POST.get("rammobile")
                screensize = request.POST.get("screensize")
                color = request.POST.get("color")
                s = MobileData(product =u,processor=processor,ram=ram,
                               screen_size=screensize,color=color)
                s.save()
            elif u.type == "laptop":
                processorlaptop = request.POST.get("processorlaptop")
                ramlaptop = request.POST.get("ramlaptop")
                hdlaptop = request.POST.get("hdlaptop")
                f = LaptopData(product =u,processor = processorlaptop,
                                ram = ramlaptop,hard_drive_capacity=hdlaptop)
                f.save()
            return render(request,"crud/home.html",{})
        return render(request,"crud/home.html",{})
    else:
        return redirect(login_view)

def logoutview(request):
    if not request.session.has_key["username"]:
        return redirect(RegisterView)
    del request.session["username"]
    return redirect(login_view)
