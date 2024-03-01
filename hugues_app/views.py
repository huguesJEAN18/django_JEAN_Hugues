from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .models import Vol, Reservation

def connexion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'connexion.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html', {'vols': vols})

def reserver_vol(request, vol_id):
    if request.method == 'POST':
        vol = Vol.objects.get(pk=vol_id)
        reservation = Reservation.objects.create(vol=vol, user=request.user)
        reservation.save()
        return redirect('toutes_reservations')  
    else:
        vol = Vol.objects.get(pk=vol_id)
        context = {'vol': vol}
        return render(request, 'reservation.html', context)


def toutes_reservations(request):
    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'toutes_reservations.html', context)



@login_required
def planifier_vol(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.utilisateur = request.user
            reservation.save()
            return redirect('suivi_vols')
    else:
        form = ReservationForm()
    return render(request, 'planifier_vol.html', {'form': form})

@login_required
def suivi_vols(request):
    reservations = Reservation.objects.filter(utilisateur=request.user)
    return render(request, 'suivi_vols.html', {'reservations': reservations})
