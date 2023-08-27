from rest_framework.pagination import PageNumberPagination


# NOTE: size smalle than products to pursuade searching through the product
#   list
class UserProfilePaginator(PageNumberPagination):
    page_size = 25
