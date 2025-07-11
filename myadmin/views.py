from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login
from .models import*


# Create your views here.

def dashboard(request):
    if request.session.get("name"):
           return render(request,'dashboard.html')
    else:     
        return redirect("/myadmin/logins")

 

def logins(request):
    if request.session.get('name'):
        return redirect('/myadmin/dashboard/')
    if request.method == 'POST':
        amd_name = request.POST.get('amd_name')
        amd_password = request.POST.get('amd_password')
        user = admin_user.objects.filter(amd_name=amd_name,amd_password=amd_password).first()
        if user:
            request.session['name']=amd_name
            return redirect('/myadmin/dashboard/')
        else:
            return redirect('/myadmin/logins/')

    return render(request,'logins.html')

def masterpage(request):
    return render(request,'masterpage.html')


def user(request):
    return render(request,'user.html')










def setting(request):
    return render(request,'setting.html')





# def admin_login(request):
#     # if request.session.get('name'):
#     #     return redirect('/myadmin/dashboard/')
#     # if request.method == 'POST':
#     #     amd_name = request.POST.get('amd_name')
#     #     amd_password = request.POST.get('amd_password')
#     #     user = admin_user.objects.filter(amd_name=amd_name,amd_password=amd_password).first()
#     #     if user:
#     #         request.session['name']=amd_name
#     #         return redirect('/myadmin/dashboard/')
#     #     else:
#     #         return redirect('myadmin/logins/')

#     return render(request,'logins.html')

def logout(request):
    request.session.flush()
    return redirect('/myadmin/logins/')


def category(request):

    tables = CategoryMaster.objects.all()

    return render(request,'category.html',{"tables":tables})

def add_new(request):
    if request.method == 'POST':

        catName = request.POST.get('catName')
        catImage = request.FILES.get('catImage')
        catSlug = request.POST.get('catSlug')
        catStatus = request.POST.get('catStatus') == 'on'   


        CategoryMaster.objects.create(
            catName=catName,
            catImage=catImage,
            catSlug=catSlug,
            catStatus=catStatus
        )
 
        return redirect('/myadmin/category/')
    return render(request,'add_new.html')
from django.shortcuts import render


def delte_category(request, id):
    query = CategoryMaster.objects.get(id = id)
    query.delete()
    return redirect("/myadmin/category/")



def update(request, id):
    if not request.session.get("name"):
        return redirect("/myadmin/logins/")
    category = get_object_or_404(CategoryMaster,id=id)

    if  request.method == 'POST':
        category.catName = request.POST.get("catName")
        category.catStatus = request.POST.get("catStatus") == 'on'
        category.catSlug = request.POST.get("catSlug")

        if 'catImage' in request.FILES:
            category.catImage = request.FILES['catImage']

        category.save()
        return redirect('/myadmin/category/')
    return render(request, 'update_category.html', {"data": category})



        



