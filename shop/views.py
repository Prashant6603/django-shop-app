from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Shop
from .forms import ShopForm
from django.contrib.auth import login
from .forms import CustomSignupForm
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm


def shop_map(request):
    """Display shop list & map with search and filters."""
    query = request.GET.get("q")
    category = request.GET.get("category")
    show_all = request.GET.get("all") == "1"

    shops = Shop.objects.all()

    if request.user.is_authenticated and not show_all:
        shops = shops.filter(owner=request.user)

    if query:
        shops = shops.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query)
        )

    if category:
        shops = shops.filter(category__icontains=category)

    return render(request, "dashboard.html", {"shops": shops})


@login_required
def create_shop(request):
    """Create a new shop for the logged-in user."""
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.owner = request.user
            shop.save()
            return redirect("shop_map")
    else:
        form = ShopForm()

    return render(request, "shop_form.html", {"form": form})


@login_required
def update_shop(request, pk):
    """Update a shop owned by the logged-in user."""
    shop = get_object_or_404(Shop, pk=pk, owner=request.user)

    if request.method == "POST":
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect("shop_map")
    else:
        form = ShopForm(instance=shop)

    return render(request, "shop_form.html", {"form": form})


@login_required
def delete_shop(request, pk):
    """Delete a shop owned by the logged-in user."""
    shop = get_object_or_404(Shop, pk=pk, owner=request.user)
    shop.delete()
    return redirect("shop_map")


@login_required
def view_shops(request):
    """Show all shops of the logged-in user in table view."""
    all_shops = Shop.objects.filter(owner=request.user)
    return render(request, "view_shop.html", {"all_shops": all_shops})


def custom_login(request):
    """Login user using custom login form."""
    if request.method == "POST":
        form = CustomLoginForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("shop_map")

    else:
        form = CustomLoginForm()

    return render(request, "login.html", {"form": form})


def signup_view(request):
    """Register a new user and auto login."""
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("shop_map")
    else:
        form = CustomSignupForm()

    return render(request, "sign_up.html", {"form": form})

