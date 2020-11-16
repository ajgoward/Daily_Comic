from django.shortcuts import (
    render, get_object_or_404, redirect, reverse, HttpResponseRedirect)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Reviews
from .forms import ReviewForm, ProductForm


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
            messages.success(
                request, 'Successfully Added Your Review! Thank You!')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def add_a_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('item_detail', args=[product.id]))
    else:
        form = ProductForm()

    template = 'products/add_a_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_the_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('item_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_the_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_the_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.warning(request, 'Product deleted!')
    return redirect(reverse('products'))
