from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

from fruitipediaApp.fruits.forms import CategoryAddForm, AddFruitForm, EditFruitFrom, DeleteFruitForm
from fruitipediaApp.fruits.models import Fruit, Category


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {'fruits': fruits}

    return render(request, 'common/dashboard.html', context)


class CreateFruitView(CreateView):
    model = Fruit
    form_class = AddFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')


def edit_fruit(request, fruit_id):
    fruit = Fruit.objects.get(pk=fruit_id)

    if request.method == 'GET':
        form = EditFruitFrom(instance=fruit)
    else:
        form = EditFruitFrom(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'fruit': fruit,
        'form': form
    }

    return render(request, 'fruits/edit-fruit.html', context)


def details_fruit(request, fruit_id):
    fruit = Fruit.objects.get(pk=fruit_id)

    context = {
        'fruit': fruit
    }

    return render(request, 'fruits/details-fruit.html', context)


def delete_fruit(request, fruit_id):
    fruit = Fruit.objects.filter(pk=fruit_id).get()

    if request.method == 'POST':
        form = DeleteFruitForm(request.POST, instance=fruit)

        if form.is_valid():
            fruit.delete()

            return redirect('dashboard')

    else:
        form = DeleteFruitForm(instance=fruit)

    context = {
        'form': form,
        'fruit': fruit,
    }

    return render(request, 'fruits/delete-fruit.html', context)


def create_category(request):
    if request.method == 'GET':
        form = CategoryAddForm()
    else:
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'categories/create-category.html', context)
