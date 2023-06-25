from django.shortcuts import render,get_object_or_404
from .models import Category,Product ,Restaurant
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    category = Category.objects.all()
    restaurants = Restaurant.objects.all()



    context = {
        'category':category,
        'restaurants':restaurants

    }

    return render(request,'central/index.html',context)

def show(request,category_slug = None):
    restaurants = Restaurant.objects.all()
    products = Product.objects.filter(available=True).order_by('-id')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
        paginator = Paginator(products, 8)  # Show 25 contacts per page.

        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)
    return render(request,'central/show.html',{'category':category,'products':products,'restaurants':restaurants})