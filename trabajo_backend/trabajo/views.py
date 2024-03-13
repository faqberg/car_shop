from django.shortcuts import render, redirect
from .models import Cars,Car_Features,Car_Info
from django.contrib import messages
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    return render(request,"index.html")

def models(request):
    filt = request.GET.get("filter", "none")
    order = request.GET.get("order", "none")
    cars=Cars.objects.all()
    for car in cars:
        car.price=int(car.price)
        car.year=int(car.year)
    return render(request, "models.html", {"filter": filt, "order": order,"cars":cars})

def model(request,carname):
    car=Cars.objects.get(name=carname)
    car_features=Car_Features.objects.filter(id_car=1).all()  #cuando se carguen los datos de cada auto se reemplaza 1 por car.id
    car_infos=Car_Info.objects.filter(id_car=1).all()   #cuando se carguen los datos de cada auto se reemplaza 1 por car.id
    return render(request,"model.html",{"car":car,"car_features":car_features,"car_infos":car_infos})

def edit(request):
    return render(request,"edit.html")

def create_car(request):
    return render(request,"create_car.html")

def create_car_form(request):
    name=request.POST["name"].capitalize()
    year=request.POST["year"]
    price=request.POST["price"]
    type=request.POST["type"]
    photo=request.POST["photo"]
    title_description=request.POST["title_description"]
    description=request.POST["description"]
    if Cars.objects.filter(name=name).exists():
        messages.info(request,"Ya está registrado un auto con este nombre.")
        return redirect("create_car")
    Cars.objects.create(name=name,year=year,price=price,type=type,photo=photo,title_description=title_description,description=description)
    messages.info(request,"El auto fué creado exitosamente.")
    return redirect("create_car")


def edit_cars(request):
    filt = request.GET.get("filter", "none")
    order = request.GET.get("order", "none")
    cars=Cars.objects.all()
    for car in cars:
        car.price=int(car.price)
        car.year=int(car.year)
    return render(request, "edit_cars.html", {"filter": filt, "order": order,"cars":cars})

def edit_car(request,carname):
    car=Cars.objects.get(name=carname)
    return render(request,"edit_car.html",{"car":car})

def edit_car_form(request):
    name=request.POST["name"].capitalize()
    year=request.POST["year"]
    price=request.POST["price"]
    type=request.POST["type"]
    photo=request.POST["photo"]
    title_description=request.POST["title_description"]
    description=request.POST["description"]
    carname=request.POST["carname"]
    car=Cars.objects.get(name=carname)
    if name!=carname and Cars.objects.filter(name=name).exists():
        messages.info(request,"Ya está registrado un auto con este nombre.")
        return redirect("edit_car/"+name)
    car.name=name
    car.year=year
    car.price=price
    car.type=type
    car.photo=photo
    car.title_description=title_description
    car.description=description
    car.save()
    messages.info(request,"El auto fué modificado exitosamente.")
    return redirect("edit_car/"+name)

def delete_cars(request):
    filt = request.GET.get("filter", "none")
    order = request.GET.get("order", "none")
    cars=Cars.objects.all()
    for car in cars:
        car.price=int(car.price)
        car.year=int(car.year)
    return render(request,"delete_cars.html", {"filter": filt, "order": order,"cars":cars})

def delete_car(request,carname):
    car=Cars.objects.get(name=carname)
    return render(request,"delete_car.html",{"car":car})

def delete_car_confirm(request):
    carname=request.POST["carname"]
    return render(request,"delete_car_confirm.html",{"carname":carname})

def delete_car_form(request):
    car=Cars.objects.get(name=request.POST["name"])
    car_features=Car_Features.objects.filter(id_car=car.id).all()
    for car_feature in car_features:
        car_feature.delete()
    car_infos=Car_Info.objects.filter(id_car=car.id).all()
    for car_info in car_infos:
        car_info.delete()
    car.delete()
    return redirect("delete_cars")
    
def edit_features(request):
    filt = request.GET.get("filter", "none")
    order = request.GET.get("order", "none")
    cars=Cars.objects.all()
    for car in cars:
        car.price=int(car.price)
        car.year=int(car.year)
    return render(request,"edit_features.html", {"filter": filt, "order": order,"cars":cars})

def edit_features_car(request,carname):
    car=Cars.objects.get(name=carname)
    car_features=Car_Features.objects.filter(id_car=car.id).all()
    num_car_features=len(car_features)
    return render(request,"edit_features_car.html",{"car":car,"car_features":car_features,"num_car_features":num_car_features})


def add_features(request,carname):
    car=Cars.objects.get(name=carname)
    return render(request,"add_features.html",{"car":car})

def add_features_form(request):
    car_id=request.POST["car_id"]
    title=request.POST["title"]
    description=request.POST["description"]
    photo=request.POST["photo"]
    new_feature=Car_Features.objects.create(id_car=car_id,title=title,description=description,photo=photo)
    new_feature.save()
    messages.info(request,"El feature fué añadido exitosamente.")
    return redirect("add_features/"+Cars.objects.get(id=car_id).name)

def edit_feature(request,featureid):
    feature=Car_Features.objects.get(id=featureid)
    car=Cars.objects.get(id=Car_Features.objects.get(id=featureid).id_car)
    return render(request,"edit_feature.html",{"feature":feature,"car":car})

def edit_feature_form(request):
    title=request.POST["title"]
    description=request.POST["description"]
    photo=request.POST["photo"]
    feature_id=request.POST["feature_id"]
    feature=Car_Features.objects.get(id=feature_id)
    feature.title=title
    feature.description=description
    feature.photo=photo
    feature.save()
    messages.info(request,"El feature fué editado con éxito.")
    return redirect("edit_feature/"+feature_id)

def delete_feature_confirm(request,featureid):
    feature=Car_Features.objects.get(id=featureid)
    car=Cars.objects.get(id=feature.id_car)
    return render(request,"delete_feature_confirm.html",{"feature":feature,"car":car})

def delete_feature_form(request):
    feature_id=request.POST["feature_id"]
    carname=request.POST["carname"]
    feature=Car_Features.objects.get(id=feature_id)
    feature.delete()
    return redirect("edit_features/"+carname)

def edit_info(request):
    filt = request.GET.get("filter", "none")
    order = request.GET.get("order", "none")
    cars=Cars.objects.all()
    for car in cars:
        car.price=int(car.price)
        car.year=int(car.year)
    return render(request,"edit_info.html", {"filter": filt, "order": order,"cars":cars})

def edit_info_car(request,carname):
    car=Cars.objects.get(name=carname)
    car_infos=Car_Info.objects.filter(id_car=car.id).all()
    num_car_info=len(car_infos)
    return render(request,"edit_info_car.html",{"car":car,"car_infos":car_infos,"num_car_infos":num_car_info})

def edit_inf(request,infoid):
    info=Car_Info.objects.get(id=infoid)
    car=Cars.objects.get(id=info.id_car)
    return render(request,"edit_inf.html",{"info":info,"car":car})

def edit_inf_form(request):
    title=request.POST["title"]
    description=request.POST["description"]
    photo=request.POST["photo"]
    info_id=request.POST["info_id"]
    info=Car_Info.objects.get(id=info_id)
    info.title=title
    info.description=description
    info.photo=photo
    info.save()
    messages.info(request,"La info fué editada exitosamente.")
    return redirect("edit_inf/"+info_id)

def delete_inf_confirm(request,infoid):
    info=Car_Info.objects.get(id=infoid)
    car=Cars.objects.get(id=info.id_car)
    return render(request,"delete_inf_confirm.html",{"info":info,"car":car})

def delete_inf_form(request):
    carname=request.POST["carname"]
    info_id=request.POST["info_id"]
    info=Car_Info.objects.get(id=info_id)
    info.delete()
    return redirect("edit_info/"+carname)

def add_info(request,carname):
    car=Cars.objects.get(name=carname)
    return render(request,"add_info.html",{"car":car})

def add_info_form(request):
    title=request.POST["title"]
    description=request.POST["description"]
    photo=request.POST["photo"]
    car_id=request.POST["car_id"]
    new_info=Car_Info.objects.create(title=title,description=description,photo=photo,id_car=car_id)
    new_info.save()
    messages.info(request,"La info fué agregada con éxito.")
    return redirect("add_infos/"+Cars.objects.get(id=car_id).name)

########    API    ##########


@csrf_exempt
def get_all_cars_api(request):
    if request.method == "GET":
        cars = Cars.objects.all().values()
        return JsonResponse({"cars": list(cars)})

@csrf_exempt
def get_car_details_api(request, pk):
    if request.method == "GET":
        try:
            car = Cars.objects.values().get(pk=pk)
            return JsonResponse({"car": car})
        except Cars.DoesNotExist:
            return JsonResponse({"error": "Car not found"}, status=404)

@csrf_exempt
def create_car_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            car = Cars.objects.create(**data)
            return JsonResponse({"message": "Car created successfully", "car_id": car.pk}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def update_car_api(request, pk):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            car = Cars.objects.get(pk=pk)
            for key, value in data.items():
                setattr(car, key, value)
            car.save()
            return JsonResponse({"message": "Car updated successfully"})
        except Cars.DoesNotExist:
            return JsonResponse({"error": "Car not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def delete_car_api(request, pk):
    if request.method == "DELETE":
        try:
            car = Cars.objects.get(pk=pk)
            car.delete()
            return JsonResponse({"message": "Car deleted successfully"})
        except Cars.DoesNotExist:
            return JsonResponse({"error": "Car not found"}, status=404)

@csrf_exempt
def get_all_car_features_api(request):
    if request.method == "GET":
        car_features = Car_Features.objects.all().values()
        return JsonResponse({"car_features": list(car_features)})

@csrf_exempt
def get_all_car_info_api(request):
    if request.method == "GET":
        car_info = Car_Info.objects.all().values()
        return JsonResponse({"car_info": list(car_info)})
    
@csrf_exempt
def update_car_feature_api(request, pk):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            feature = Car_Features.objects.get(pk=pk)
            for key, value in data.items():
                setattr(feature, key, value)
            feature.save()
            return JsonResponse({"message": "Car feature updated successfully"})
        except Car_Features.DoesNotExist:
            return JsonResponse({"error": "Car feature not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def delete_car_feature_api(request, pk):
    if request.method == "DELETE":
        try:
            feature = Car_Features.objects.get(pk=pk)
            feature.delete()
            return JsonResponse({"message": "Car feature deleted successfully"})
        except Car_Features.DoesNotExist:
            return JsonResponse({"error": "Car feature not found"}, status=404)

@csrf_exempt
def update_car_info_api(request, pk):
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            info = Car_Info.objects.get(pk=pk)
            for key, value in data.items():
                setattr(info, key, value)
            info.save()
            return JsonResponse({"message": "Car info updated successfully"})
        except Car_Info.DoesNotExist:
            return JsonResponse({"error": "Car info not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
def delete_car_info_api(request, pk):
    if request.method == "DELETE":
        try:
            info = Car_Info.objects.get(pk=pk)
            info.delete()
            return JsonResponse({"message": "Car info deleted successfully"})
        except Car_Info.DoesNotExist:
            return JsonResponse({"error": "Car info not found"}, status=404)