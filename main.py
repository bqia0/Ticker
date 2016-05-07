import ystockquote
import max7219.led as led
import time
from decimal import Decimal
stock_list= ['%5EIXIC', '%5EGSPC', 'INCY']
device = led.matrix(cascaded = 4)
device.brightness(1)
    
def get_time():
    return time.strftime("%I:%M")
def get_percent_change(symbol):
    change = ystockquote.get_change(symbol)
    price = ystockquote.get_price(symbol)
    percent_change = 100*float(change)/(float(price)-float(change))
    percent_decimal = round(Decimal(percent_change), 2)
    if percent_decimal > 0:
        return '+'+str(percent_decimal)
    elif percent_decimal==0:
        return '0'
    else:
        return '-'+str(abs(percent_decimal))
def stocks():
    stock_output = ''
    for stock in stock_list:
        #print(stock)
        #print(get_percent_change(stock))
        stock_output = stock_output+stock+' '+get_percent_change(stock)+' '
        #stock_output = stock_output+' '+get_percent_change(stock)
    return stock_output


        


#print(get_percent_change('GOOG'))
#print(get_percent_change('INCY'))
#print isinstance(get_percent_change('INCY'), str)
while True:
    device.show_message(stocks())
