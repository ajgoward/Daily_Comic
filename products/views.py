from django.shortcuts import (
    render, get_object_or_404, redirect, reverse, HttpResponseRedirect)
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Reviews
from .forms import ReviewForm


def all_stock(request):
    """ A view to show all products """
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    queryset = None

    if request.GET:

        if 'qset' in request.GET:
            queryset = request.GET['qset']
            thequery = Q(
                universe__contains=queryset) | Q(hero__icontains=queryset)
            products = products.filter(thequery)
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def item_detail(request, product_id):
    """ A veiw to show individual items """
    product = get_object_or_404(Product, pk=product_id)
    reviews = Reviews.objects.filter(product=product_id)
    form = ReviewForm()
    context = {
        'product': product,
        'reviews': reviews,
        'form': form,
    }

    return render(request, 'products/item-detail.html', context)


def Add_Review(request):
    """ Add a product to the store """

    if request.method == 'POST':

        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
