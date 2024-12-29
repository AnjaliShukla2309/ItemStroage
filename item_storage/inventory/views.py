
from django.shortcuts import render
from .models import Item
from django.core.paginator import Paginator

def item_list(request):
    sort_by = request.GET.get('sort', 'name')  # Sorting by name, price, or created_at
    item_list = Item.objects.all().order_by(sort_by)

    # Pagination
    paginator = Paginator(item_list, 4)  # Show items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'sort_by': sort_by
    }
    return render(request, 'item_list.html', context)

