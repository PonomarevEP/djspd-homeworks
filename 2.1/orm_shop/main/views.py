from django.http import Http404
from django.shortcuts import render

from main.models import Car, Sale, Client
import shutil


def cars_list_view(request):
    cars = Car.objects.all()
    if not cars.exists():
        source_file = r"C:\Users\ponom\OneDrive\Desktop\DJ_auto\djspd-homeworks\2.1\images\toyota_camry.jpg"
        target_file = r"C:\Users\ponom\OneDrive\Desktop\DJ_auto\djspd-homeworks\2.1\orm_shop\media\images\toyota_camry.jpg"
        shutil.copy(source_file, target_file)
        Car.objects.create(
            id = 1,
            model = "Toyota Camry",
            year = 2019,
            color = "Черный",
            mileage = 100000,
            volume = 3.5,
            body_type = "sedan",
            drive_unit = "front",
            gearbox = "automatic",
            fuel_type = "gasoline", 
            price = 570000,
            image = "images/toyota_camry.jpg"
        )

        source_file = r"C:\Users\ponom\OneDrive\Desktop\DJ_auto\djspd-homeworks\2.1\images\vesta_sw_cross.jpg"
        target_file = r"C:\Users\ponom\OneDrive\Desktop\DJ_auto\djspd-homeworks\2.1\orm_shop\media\images\vesta_sw_cross.jpg"
        shutil.copy(source_file, target_file)
        Car.objects.create(
            id = 2,
            model = "Lada Vesta Cross",
            year = 2022,
            color = "Серый",
            mileage = 50000,
            volume = 1.6,
            body_type = "wagon",
            drive_unit = "front",
            gearbox = "manual",
            fuel_type = "gasoline", 
            price = 350000,
            image = "images/vesta_sw_cross.jpg"
        )

        source_file = r"C:\Users\ponom\OneDrive\Desktop\DJ_auto\djspd-homeworks\2.1\images\mb_s_classe.jpg"
        target_file = r"C:\Users\ponom\OneDrive\Desktop\DJ_auto\djspd-homeworks\2.1\orm_shop\media\images\mb_s_classe.jpg"
        shutil.copy(source_file, target_file)
        Car.objects.create(
            id = 3,
            model = "mb_s_classe",
            year = 2023,
            color = "Серебристый",
            mileage = 500000,
            volume = 5.0,
            body_type = "coupe",
            drive_unit = "full",
            gearbox = "automatic",
            fuel_type = "gasoline", 
            price = 1400000,
            image = "images/mb_s_classe.jpg"
        )   
    return render(request, 'main/list.html', {'cars': cars})


def car_details_view(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404("Автомобиль с данным ID не существует")

    return render(request, 'main/details.html', {'car': car}) 


def sales_by_car(request, car_id):
    try:
        car = Car.objects.get(pk=car_id)
    except Car.DoesNotExist:
        raise Http404('Car not found')
    
    sales = Sale.objects.filter(car=car)
    if not sales.exists():
        client1 = Client.objects.create(name="Иван", last_name="Иванов", middle_name="Иванович", date_of_birth="2000-01-01", phone_number="+79998887766")
        client2 = Client.objects.create(name="Петр", last_name="Петров", middle_name="Петрович", date_of_birth="1990-02-02", phone_number="+79997776655")
        
        sale1 = Sale.objects.create(client=client1, car=car)
        sale2 = Sale.objects.create(client=client2, car=car)

        sales = Sale.objects.filter(car=car)
    
    return render(request, 'main/sales.html', {'sales': sales, 'car': car})  
