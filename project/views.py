from django.shortcuts import render, redirect
from django.http import HttpResponse
from yahoofinancials import YahooFinancials
from project.models import Stock, Price, DateRecord
from .forms import FormName

# Create your views here.
def index(request):
    # return HttpResponse('Hello World!')
    stock_list = Price.objects.order_by('stock_name')
    price_dict = {'price_record': stock_list}
    return render(request, 'project/index.html', context=price_dict)

def stock_detail(stock_name):
    stock_dict = {}

    yahoo_financial = YahooFinancials(stock_name)
    current_price = yahoo_financial.get_current_price()
    fifty_two_week_high_value = yahoo_financial.get_yearly_high()
    fifty_two_week_low_value = yahoo_financial.get_yearly_low()

    stock_dict['stock_name'] = stock_name
    stock_dict['high_value'] = fifty_two_week_high_value
    stock_dict['low_value'] = fifty_two_week_low_value
    stock_dict['current_price'] = current_price
    return stock_dict

def view_stock(request):

    if request.method == 'POST':
        stock_name = request.POST['stock_name']
    return render(request, 'project/stock_page.html', context=stock_detail(stock_name))

def help_page(request):
    help_content = {'email_id': 'shahrukheqbal@gmail.com'}
    return render(request, "project/help.html", context=help_content)

def form_name_view(request):
    form = FormName()
    stocks = []
    tcs_stock = stock_detail('TCS.NS')
    principal_stock = stock_detail('PFG')
    icici_stock = stock_detail('ICICIBANK.NS')
    stocks.append(tcs_stock)
    stocks.append(principal_stock)
    stocks.append(icici_stock)

    print(stocks)
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESSFUL")
            print("Stock Name: " + form.cleaned_data['stock_name'])
    return render(request, 'project/form_page.html', {'form': form, 'stocks': stocks})
