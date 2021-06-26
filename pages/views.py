from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor
from listings.choice import state_choices, price_choices, bedroom_choices

def index(request):
    listings = Listing.objects.order_by('list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'state_choices' : state_choices,
        'price_choices' : price_choices,
        'bedrooms_choices' : bedroom_choices
    }
    return render(request, 'pages/index.html', context)

def about(request):
    # Getting all realtors
    realtors = Realtor.objects.order_by('hire_date')

    # Getting seller of the month
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors' : realtors,
        'mvp_realtor': mvp_realtor
    }

    return render(request, 'pages/about.html', context)

