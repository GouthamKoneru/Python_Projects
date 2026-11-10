from datetime import datetime

name=input('Enter your name:')

#list of items
lists='''
    Rice    Rs 20/kg
    Sugar   Rs 30/kg
    Salt    Rs 20/kg
    Oil     Rs 90/liter
    Paneer  Rs 110/kg
    Maggie  Rs 50/kg
    Boost   Rs 90/each
    Colgate Rs 150/each

'''
#declaration
price=0
pricelist=[]
totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={
    'Rice':20, 
    'Sugar':30, 
    'Salt':20, 
    'Oil':90,
    'Paneer':110,
    'Maggie':50,
    'Boost':90,
    'Colgate':150
}

option = int(input("For List of items enter 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input('if you want to buy enter 1 or 2 to exit:'))
    if inp1==2:
        break
    if inp1==1:
        item=input('Enter your items:')
        quantity=int(input('Enter the items quantity:'))
        if item in items.keys():
            price=quantity*items[item]
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=gst+totalprice
        else:
            print('The entered item is not available')
    else:
        print('entered the wrong input')
    inp=input('would you like to get the receipt yes or no: ')
    if inp=='yes':
        pass
    if finalprice!=0:
        print(25*'=','Goutham\'s Supermarket',25*'=')
        print(34*' ','Tirupati')
        print('Name:',name,30*' ','Date',datetime.now())
        print(75*'-')
        print('Sno',16*' ','Items',14*' ','Quantity',15*' ','Price')
        for i in range(len(pricelist)):
            print(i,8*' ',10*' ',ilist[i],18*' ',qlist[i],20*' ',plist[i])
        print(75*"-")
        print('Totalprice:',50*' ','Rs',totalprice)
        print('Gst amount:',50*' ', 'Rs',gst)
        print(75*"-")
        print('Finalprice:',50*' ','Rs',finalprice)
        print(75*"-")
        print(24*' ','Thanks for coming see you again',24*'')
        print(75*"-")
        