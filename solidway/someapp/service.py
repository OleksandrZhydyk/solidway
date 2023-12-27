
# A place for business logic

class SomeModelService:
    def __init__(self, repository):
        self.repository = repository

    def get_items(self, page: int, per_page: int):
        return self.repository.get_items(page, per_page)
