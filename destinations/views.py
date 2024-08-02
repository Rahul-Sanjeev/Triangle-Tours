from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination
from .serializers import DestinationSerializer
from .forms import DestinationForm

# Create your views here.


def destination_create(request):
    if request.method == "POST":
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("destination_list")
    else:
        form = DestinationForm()
    return render(request, "destination_form.html", {"form": form})


def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, "destination_list.html", {"destinations": destinations})


def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, "destination_details.html", {"destination": destination})


def destination_update(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == "POST":
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            form.save()
            return redirect("destination_list")
    else:
        form = DestinationForm(instance=destination)
    return render(request, "destination_form.html", {"form": form})


def destination_delete(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == "POST":
        destination.delete()
        return redirect("destination_list")
    return render(request, "destination_delete.html", {"destination": destination})


def base(request):
    return render(request, "base.html")
