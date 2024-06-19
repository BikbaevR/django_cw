from django.shortcuts import render, redirect
from .models import *

def index(request):

    return render(request, 'hotel/index.html')


def create_room_type(request):
    if request.method == 'POST':
        room_type = request.POST['room_type']
        room = RoomType(name=room_type)
        room.save()
        return redirect('create_room_type')

    context = {'room_type': RoomType.objects.all()}
    return render(request, 'hotel/create_room_type.html', context)


def create_room(request):
    if request.method == 'POST':
        number = request.POST['number']
        type = request.POST['type']
        price = request.POST['price']
        description = request.POST['description']
        photo = request.FILES['photo']

        room_type = RoomType.objects.get(pk=type)
        new_room = HotelRoom(number=number, type=room_type, price=price, description=description, photo=photo)
        new_room.save()
        return redirect('create_room')

    context = {'rooms': HotelRoom.objects.all(),
               'room_types': RoomType.objects.all()}
    return render(request, 'hotel/create_room.html', context)



def create_reservation(request):
    if request.method == 'POST':
        number = request.POST['number']
        date_start = request.POST['date_start']
        date_end = request.POST['date_end']
        user = request.POST['user']

        room_obj = HotelRoom.objects.get(pk=number)
        user_obj = User.objects.get(pk=user)

        new_reservation = Reservation.objects.create(room=room_obj, date_start=date_start, date_end=date_end)
        new_reservation.user = user_obj

        new_reservation.save()
        return redirect('create_reservation')

    context = {'reservations': Reservation.objects.all(),
               'rooms': HotelRoom.objects.all()}


    return render(request, 'hotel/create_reservation.html', context)
