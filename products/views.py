from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

from profiles.permissions import HasProfileOrReadOnly

from .paginators import ProductPaginator


class ProductListApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ProductPaginator()

    "returns list of products, will check kwargs for filter"
    # TODO: decide on list of acceptable filter params
    """
    acceptable filters atm:
        - username
        - category
        - status_category
    """

    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class ProductDetailApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass
