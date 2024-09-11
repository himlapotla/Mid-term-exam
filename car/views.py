from django.shortcuts import render, get_object_or_404, redirect
from car.models import Car, Brand
from .forms import CommentForm

# Create your views here.
def show_car(request):
    car = Car.objects.all()
    return render(request, 'home.html', {'car':car})

def car_brand(request, nm):
    brand = Brand.objects.filter(name=nm).first()
    cars = Car.objects.filter(car_brand=brand)
    return render(request, 'home.html', {'car': cars})

def vd(request, id):
    carr = Car.objects.get(pk = id)
    comments = carr.comments.all()
    # return render(request, 'car.html', {'car': carr})

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user  # Attach the logged-in user
            new_comment.car = carr  # Attach the car to the comment
            new_comment.save()
            return redirect('vd', id=id)  # Redirect to the same page after submission
    else:
        comment_form = CommentForm()
    
    return render(request, 'car.html', {'car': carr, 'comments': comments, 'comment_form': comment_form})

