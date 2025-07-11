from django.shortcuts import redirect,render
from.models import*


# Create your views here.



def home(request):
    return render(request,'mini.html')


def about(request):
    return render(request,'about.html')



def contact(request):
    return render(request,'contact.html')


# def login(request):
#     if request.method ==  "POST":
#         username =request.POST.get("username")
#         password = request.POST.get("password")
#         user = User.objects.filter(username=username).first()
#         if user:
#             pwd = check_password(password, user.password) # type: ignore
#             if pwd :
#                 print("login successful")
#                 return redirect('/food/') # type: ignore
#             else:
#                 print("invalid password")

#         else:        
#             print("user not found")
        
#     return render(request,"login1.html")


# from django.contrib.auth.models import User # type: ignore


def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if first_name and last_name and username and password:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password
            )
            
            user.save()
            return redirect('login') # type: ignore
        else:
            error_message = "Please fill in all fields."
            return render(request, "register.html", {"error": error_message})
     

    return render(request,"register1.html")


# def login(request):
#     return render(request,'login1.html')

# def register(request): 
#     return render(request,'register1.html')

# def rs(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         image = request.FILES.get("image")
    
#         rs.objects.create(
#             name = name,
#             description = description,
#             image = image,

#         )

#     tables = rs.objects.all()
#     return render(request,"mini.html")



def W_home(request):
    return render(request, 'W_home.html')


def W_about(request):
    return render(request,"W_about.html")


def W_shop(request):
    return render(request,"W_shop.html")



def W_contact(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email=request.POST.get("email")
        massage=request.POST.get("massage")

        contect_now.objects.create(
            name=name,
            email=email,
            massage=massage,
        )
    return render(request,"W_contact.html")


from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

def login(request):
    if request.method ==  "POST":
        username =request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username).first()
        if user:
            pwd = check_password(password, user.password) # type: ignore
            if pwd :
                print("login successful")
                return redirect('/W_home/') # type: ignore
            else:
                print("invalid password")

        else:        
            print("user not found")
        
    return render(request,"login.html")




       
def  sign_up(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if name and email and username and password:
            user = User.objects.create_user(
                first_name=name,
                email=email,
                username=username,
                password=password
            )
            user.set_password(password)
            user.save()
            return redirect('/login/')
        else:
            print("please fill all fields")
     

    return render(request,"sign_up.html")


    


