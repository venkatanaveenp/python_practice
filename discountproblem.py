 #3. Mr.Kumar went to purchase stationary items for his office. He asked the shopkeeper for a discount. The shopkeeper said that if he purchases more than 200 quantity of the item, then a discount of 20% can be applied on the total bill amount, excluding the GST.
#Get the Quantity and price per item as an input and calculate and tell whether Mr.Kumar is eligible for the discount and what would be the net amount he has to pay after the discount.
#Take the GST at 18%.
#Net Amount = Total bill amount after discount + GST
 
amount=int(input("enter the amount="))
quntity=int(input("enter the quntity"))

if quntity>=200:
    discount=(amount*quntity*20)/100
    print("discount",discount)
    bill=amount-discount
    print("bill paid is",bill)
else:
    discount=0
    print("discount",discount)
    print("gst")
    gst=(amount*quntity*18)/100
    print("gst",gst)
    bill=(amount*quntity)+gst
    print("bill paid is",bill)
    
    