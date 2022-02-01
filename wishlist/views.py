from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse

from products.models import Product
from wishlist.models import WishList
# Create your views here.

@login_required
def wishlist(request):
    return render(request, "wishlist/wishlist.html")

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    user_wishlist = WishList.objects.filter(user_id=request.user.id, product=product)
    if user_wishlist.exists():
        user_wishlist.delete()
        messages.success(request, product.name + " has been removed from your WishList")
    else:
        WishList.objects.create(product=product, user=request.user)
        messages.success(request, "Added " + product.name + " to your WishList")
    return HttpResponseRedirect(request.META["HTTP_REFERER"])



@login_required
def remove_from_wishlist(request, wishlist_id):
    try:
        wishlist = get_object_or_404(WishList, id=wishlist_id, user_id=request.user.id)
        wishlist.delete()
    except Exception as e:
        return JsonResponse({'success':'0'})
    else:
        return JsonResponse({'success':'1'})