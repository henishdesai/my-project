from django.shortcuts import render # type: ignore
from .models import *
from django.contrib.auth.hashers import *
# Create your views here.


def contect_page(request):
    if request.method =="POST":
        name = request.POST.get("name")
        email=request.POST.get("email")
        contect=request.POST.get("contect")
        massage=request.POST.get("massage")

        contect1.objects.create(
            name=name,
            email=email,
            contect=contect,
            massage=massage
            
        )
    return render(request,"contect2.html")




def food(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
    
        recipe.objects.create(
            name = name,
            description = description,
            image = image
        )

    tables = recipe.objects.all()
    return render(request,"recipe.html",{"tables":tables})




     
# from django.shortcuts import redirect

# def delete_recipe(request,recipe_id):
#     if request.method =="POST":
#         recipe=recipe.object.get(id=recipe_id)
#         recipe.delete()
#         return redirect('food')




from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
# from django.views.decorators.http import require_POST


def delete_recipe(request,recipe_id):
    recipe_to_delete = get_object_or_404(recipe,id=recipe_id)
    recipe_to_delete.delete()
    return redirect("food")



# @require_http_methods(["GET", "POST"])
def update_recipe(request, id):
    recipe_instance = recipe.objects.get(id=id)    
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        recipe_instance.name = name
        recipe_instance.description = description

        if image:
            recipe_instance.image = image
        recipe_instance.save()
        return redirect('/food/')

    return render(request, "update_racipe.html", {"recipe": recipe_instance})




def login(request):
    if request.method ==  "POST":
        username =request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username).first()
        if user:
            pwd = check_password(password, user.password)
            if pwd :
                print("login successful")
                return redirect('/food/')
            else:
                print("invalid password")

        else:
            print("user not found")
        
    return render(request,"login_page.html")


from django.contrib.auth.models import User # type: ignore


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
            return redirect('login')
        else:
            error_message = "Please fill in all fields."
            return render(request, "register.html", {"error": error_message})
     

    return render(request,"register.html")




