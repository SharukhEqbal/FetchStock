from django.shortcuts import render, redirect
from django.http import HttpResponse
from yahoofinancials import YahooFinancials
from project.models import Stock, Price, DateRecord, StockCode
from .forms import FormName


# Create your views here.


def index(request):
    # return HttpResponse('Hello World!')
    form = FormName(request.POST)
    stock_list = Price.objects.order_by('stock_name')
    stock_code = StockCode.objects.order_by('stock_name')

    final_list = []
    price_dict = {'price_record': stock_list}
    stock_dict = {'stock_record': stock_code}
    print(price_dict)
    print(stock_dict)
    for stock in stock_list:
        stock_data = {'stock_code': stock.stock_name.stock_name, 'Current_price': stock.current_price,
                      'Max_price': stock.max_price, 'Min_price': stock.min_price}
        for stock_c in StockCode.objects.all():
            if stock_c.stock_name.stock_name == stock.stock_name.stock_name:
                stock_data['stock_name'] = stock_c.code
        final_list.append(stock_data)
    print(final_list)

    flag = 'index'
    if request.method == 'POST':
        flag = 'view'
        stock_name = request.POST['stock_name']
        stock = stock_detail(stock_name)
        print(stock['current_price'])
        print(request.method)
        # return render(request, 'project/stock_page.html', context=stock)
        if stock['current_price']:
            #return render(request, 'project/stock_page.html', context=stock)
            return render(request, 'project/index.html', {'dict1': price_dict, 'dict2': final_list, 'dict3': stock_dict,
                                                          'form': form, 'not_found': False, 'flag': flag,
                                                          'stock': stock})
        else:
            return render(request, 'project/index.html', {'dict1': price_dict, 'dict2': final_list, 'dict3': stock_dict,
                                                          'form': form, 'not_found': True, 'flag': flag})
    else:
        return render(request, 'project/index.html', {'dict1': price_dict, 'dict2': final_list, 'dict3': stock_dict,
                                                      'form': form, 'flag': flag})

    # return render(request, 'project/index.html', context=price_dict)


def stock_detail(stock_name):
    stock_dict = {}

    yahoo_financial = YahooFinancials(stock_name)
    current_price = yahoo_financial.get_Current_price()
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
    stock = stock_detail(stock_name)
    not_found = True
    print(stock.current_price)
    print(request.method)
    return render(request, 'project/stock_page.html', context=stock)
    # if stock['current_price']:
    #    return render(request, 'project/stock_page.html', {'stock_detail': stock, 'message': 'Data Available'})
    # else:
    #    return render(request, 'project/index.html', {'message': 'No Data'})


def help_page(request):
    help_content = {'email_id': 'shahrukheqbal@gmail.com'}
    return render(request, "project/help.html", context=help_content)


def form_name_view(request):
    form = FormName()
    stocks = []
    tcs_stock = stock_detail('TCS.NS')
    # principal_stock = stock_detail('PFG')
    # icici_stock = stock_detail('ICICIBANK.NS')
    stocks.append(tcs_stock)
    # stocks.append(principal_stock)
    # stocks.append(icici_stock)

    print(stocks)
    if request.method == 'POST':
        form = FormName(request.POST)
        if form.is_valid():
            # DO SOMETHING CODE
            print("VALIDATION SUCCESSFUL")
            print("Stock Name: " + form.cleaned_data['stock_name'])
            # stock_name = request.POST['stock_name']
            # return render(request, 'project/stock_page.html', context=stock_detail(stock_name))
            # return redirect('project/stock_page.html', context=stock_detail(stock_name))
    # else:
    return render(request, 'project/form_page.html', {'form': form, 'stocks': stocks})
