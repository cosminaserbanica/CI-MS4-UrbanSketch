from django.urls import path
from . import views
from bag import views as bag_views

urlpatterns = [
    path("", views.wishlist, name="wishlist"),
    path('add_bag/<item_id>/', bag_views.add_to_bag, name='add_bag'),
    path('remove/<wishlist_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist')
]