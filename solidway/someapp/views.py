from django.http import JsonResponse
from django.views import View

from someapp.repository import SomeModelRepository
from someapp.service import SomeModelService

# Can be initialized via DI container
some_model_service = SomeModelService(SomeModelRepository)


class SomeModelView(View):
    default_items_per_page = "10"
    default_page = "1"

    def get(self, request):
        page = request.GET.get("page", self.default_page)
        per_page = request.GET.get("per_page", self.default_items_per_page)
        if not self._is_params_valid(page, per_page):
            return JsonResponse({"error": "Invalid value for param"}, status=400)
        data = some_model_service.get_items(int(page), int(per_page))
        return JsonResponse(data, safe=False, status=200)

    def _is_params_valid(self, page: str, per_page: str) -> bool:
        return all([page.isdigit(), per_page.isdigit()])
