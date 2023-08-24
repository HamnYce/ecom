from rest_framework.pagination import PageNumberPagination


class UserProfilePaginator(PageNumberPagination):
    page_size = 100
