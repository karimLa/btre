from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


from .choices import bedroom_choices, price_choices, state_choices
from .models import Listing

def index(request):
  listings = Listing.objects.order_by('-list_date').filter(is_published=True)

  paginator = Paginator(listings, 6)
  page = request.GET.get('page')
  paged_listings = paginator.get_page(page)

  context = {
    'listings': paged_listings
  }
  
  return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
  listing = get_object_or_404(Listing, pk=listing_id)

  context = {
    'listing': listing
  }

  return render(request, 'listings/listing.html', context)


def search(request):
  query_list = Listing.objects.order_by('-list_date')

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      query_list = query_list.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    keywords = request.GET['city']
    if keywords:
      query_list = query_list.filter(city__iexact=keywords)
  
  # State
  if 'state' in request.GET:
    keywords = request.GET['state']
    if keywords:
      query_list = query_list.filter(state__iexact=keywords)

  # Bedrooms
  if 'bedrooms' in request.GET:
    keywords = request.GET['bedrooms']
    if keywords:
      query_list = query_list.filter(bedrooms__lte=keywords)
  
  # Price
  if 'price' in request.GET:
    keywords = request.GET['price']
    if keywords:
      query_list = query_list.filter(price__lte=keywords)

  context = {
    'bedroom_choices': bedroom_choices,
    'price_choices': price_choices,
    'state_choices': state_choices,
    'listings': query_list,
    'values': request.GET,
  }

  return render(request, 'listings/search.html', context)
