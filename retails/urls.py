from django.urls import path
from . import views

urlpatterns = [
    path('client_number_one/', views.client_number_one_view),
    path('product_sold_most/', views.product_sold_most_view),
    # path('ration_price_quantity/', views.listing_invoice_ratio_view),
    path('groupeby_invoice_ratio/', views.listing_invoice_ratio_view),
    path('groupeby_invoice/', views.groupeby_invoice_view),
]
