from django.core.paginator import Paginator, EmptyPage

from someapp.models import SomeModel


class SomeModelRepository:
    def get_items(self, page: int, per_page: int):
        items_queryset = SomeModel.objects.all()
        paginator = Paginator(items_queryset, per_page)
        try:
            items = paginator.page(page)
        except EmptyPage:
            # If the page is out of range, show the last page
            items = paginator.page(paginator.num_pages)
        return items
