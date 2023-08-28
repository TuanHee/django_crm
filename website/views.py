from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def home(request):
    records = Record.objects.all()
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records': records})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered, welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})


def record_create(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                store_record = form.save()
                messages.success(request, "Record added successfully.")
                return redirect('home')
        return render(request, 'create.html', {'form': form})
    messages.success(request, "You must be logged in to do that...")
    return redirect('home')


def records_show(request, id):
    if request.user.is_authenticated:
        # look up records
        record = Record.objects.get(id=id)
        return render(request, 'record.html', {'record': record})
    else:
        messages.success(request, "YOur must be logged in to view that page")
        return redirect('home')


def records_update(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        form = AddRecordForm(request.POST or None, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record update successfully.")
            return redirect('home')
        return render(request, 'edit.html', {'form': form})
    messages.success(request, "You must be logged in to do that...")
    return redirect('home')


def records_delete(request, id):
    if request.user.is_authenticated:
        record = Record.objects.get(id=id)
        record.delete()
        messages.success(request, "Record delete successfully.")
        return redirect('home')
    messages.success(request, "You must be logged in to do that...")
    return redirect('home')