# spa/views.py
from django.shortcuts import render,get_object_or_404
from .models import *
from .forms import SpaSearchForm
from django.db.models import Q
# def spa_search(request):
#     all = SpaCenter.objects.all()
#     if request.method == 'POST':
#         form = SpaSearchForm(request.POST)
#         if form.is_valid():
#             keyword = form.cleaned_data['keyword']
#             spa_centers = SpaCenter.objects.filter(Q(name__icontains=keyword) | Q(address__icontains=keyword))
#             return render(request, 'result.html', {'spa_centers': spa_centers, 'form': form})
#     else:
#         form = SpaSearchForm()
#     return render(request, 'index.html', {'form': form,'all':all})




def spa_search(request):
    all = SpaCenter.objects.all()
    
    if request.method == 'POST':
        form = SpaSearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            # Split the keyword into individual words
            keywords_list = keyword.split()
            # Create a list of Q objects to search for each keyword in relevant fields
            queries = [Q(name__icontains=word) | Q(description__icontains=word) | Q(address__icontains=word) for word in keywords_list]
            # Combine all Q objects using logical OR operator
            combined_query = Q()
            for query in queries:
                combined_query |= query
            # Filter SpaCenter objects using the combined query
            spa_centers = SpaCenter.objects.filter(combined_query)
            return render(request, 'result.html', {'spa_centers': spa_centers, 'form': form})
    else:
        form = SpaSearchForm()
    
    return render(request, 'index.html', {'form': form, 'all': all})

def spa_details(request, spa_id):
    spa_center = get_object_or_404(SpaCenter, pk=spa_id)
    return render(request, 'indexing.html', {'spa_center': spa_center})