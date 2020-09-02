from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Order 



# Create your views here.
def ordered(request):
    if request.method == 'POST':
        
        # get values of order form
        item = request.POST['item']
        client = request.POST['client']
        amount = request.POST['amount']
        phone = request.POST['phone']
        email = request.POST['email']
        description = request.POST['description']

        order = Order(client=client, item=item, phone=phone, email=email, amount=amount,description=description)

        order.save()

        send_mail(
            'New order Senper Graphics',
            'Dear senper graphics admin, there has been new order made through your website. log in to the admin dashboard for detail. good bye!',
            'geme8611@gmail.com',
            [
                'gemg2019@gmail.com',
                'joyigirma@gmail.com'
            ],
            fail_silently=False

        )

        messages.success( request, 'your order has been taken! we will get back to you very soon!')
    
        return redirect('index')

def order_form(request):
    return render(request, 'order/order.html')