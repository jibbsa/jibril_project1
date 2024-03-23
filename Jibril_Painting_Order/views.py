from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Painting, Order  

def order_form(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            # Instantiate a new Order object from the form data
            new_order = Order(
                player_name=form.cleaned_data['player_name'],
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],  # Reminder: Handle passwords securely.
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                province=form.cleaned_data['province'],
                postal_code=form.cleaned_data['postal_code'],
                painting=form.cleaned_data['painting']
            )
            # Save the new Order to the database
            new_order.save()
            # Redirect to a confirmation page or back to the form
            return redirect('order_confirmation', order_id=new_order.id)
    else:
        form = OrderForm()
    return render(request, 'Jibril_Form.html', {'form': form})
