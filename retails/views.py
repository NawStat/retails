from os import listdir
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from retails.apps import spark_dataframe
from django.views import View
import retails.utils as utils
import json
from retails.spark_utils import IMAGE_PATH
from django.views.generic import DetailView

@login_required
def groupeby_invoice_view(request):
    """
    Return the data for each invoice paginated
    """
    data = spark_dataframe.get_data()
    # data per Invoice
    result = utils.data_per_invoice(data)
    paginator = Paginator(result, 4) # Show 4 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_invoices.html', {'page_obj': page_obj})

@login_required
def client_number_one_view(request):
    """
    Return a view of which customer spent the most money
    """
    customer_max = spark_dataframe.first_customer()
    return HttpResponse(json.dumps({"value": customer_max}), content_type='application/json')

@login_required
def product_sold_most_view(request):
    """
    Return a view product sold the most
    """
    product_sold_most = spark_dataframe.product_sold_most()
    result = {}
    result['InvoiceNo'] = product_sold_most.InvoiceNo
    result['SumQuantity'] = product_sold_most.sum_quantity
    return HttpResponse(json.dumps(result), content_type='application/json')

@login_required
def ratio_price_quantity_view(request):
    """
    Return the ratio between price and quantity for each invoice
    Notice: this to list all in one page
    """
    ration_price_quantity = spark_dataframe.ration_price_quantity()
    # ratios per Invoice
    result = utils.ratios_per_invoice(ration_price_quantity)
    return HttpResponse(json.dumps(result), content_type='application/json')

@login_required
def listing_invoice_ratio_view(request):
    """
    Return the ratio between price and quantity for each invoice paginated
    """
    ration_price_quantity = spark_dataframe.ration_price_quantity()
    # ratios per Invoice
    result = utils.ratios_per_invoice(ration_price_quantity)
    paginator = Paginator(result, 20) # Show 20 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_invoices_ratio.html', {'page_obj': page_obj})


class ProductDistribution(LoginRequiredMixin, DetailView):

    def post(self, request):
        labels = []
        stock_code = request.POST.get('stockCode')
        self.request.session['stock_code'] = stock_code
        images = listdir(IMAGE_PATH)
        if len(images) < 25:
            if str(stock_code)+'.png' not in images:
                spark_dataframe.image_product_distribution_by_country(stock_code)
        return render(request, 'data_visualisation.html',
                      {'stock_code': stock_code, 'image_path': str(stock_code)+'.png'})

    def get(self, request):
        return render(request, 'data_visualisation.html', {'stock_code': '22728'})

    # def get_context_data(self, **kwargs):

