from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
import rest_framework.status as status

from profiles.permissions import HasProfileOrReadOnly

from .paginators import ProductPaginator
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# TODO: url product/u/<str:username>/ that routes to users products
# TODO: decide on list of acceptable filter params
# TODO: add if statements with filter for queryset then page at the end


class ProductListApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = ProductPaginator()

    "returns list of products, will check kwargs for filter"
    """
    acceptable filters atm:
        - category
        - status_category

        - not username as that can be done through the specified endpoint
    """

    def get(self, request: Request, *args, **kwargs):
        queryset = Product.objects.all()

        #   filters suupplied in request.queryparams.get()

        page = self.pagination_class.paginate_queryset(
            queryset=queryset, request=request)
        if page is not None:
            serializer = ProductSerializer(page, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        data = request.POST.dict()
        serializer = ProductSerializer(data=data)
        print(request.user)

        if serializer.is_valid():
            serializer.save(owner=request.user.userprofile)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailApiView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass


class CategoryListApiView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = CategorySerializer(Category.objects.all(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
