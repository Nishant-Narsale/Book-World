from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductsSerializer
from main.models import Products



@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'View Products' : 'api/products/',
        'Create New Product' : 'api/create-product/',
        'Update Existing Product' : 'api/update-product/product_id(e.g. 2)/',
        'Delete Existing Product' : 'api/delete-product/product_id(e.g. 2)/'
    }
    return Response(api_urls)

@api_view(['GET'])
def ProductsView(request):
    products = Products.objects.all()
    serializer = ProductsSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def CreateProduct(request):
    serializer = ProductsSerializer(data=request.data)

    if not serializer.is_valid():
        return Response('Invalid data')
        
    serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateProduct(request,id):
    product = Products.objects.get(id=id)
    serializer = ProductsSerializer(instance=product, data=request.data)

    if not serializer.is_valid():
        return Response('Invalid data')

    serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteProduct(request,id):
    product = Products.objects.get(id=id)
    product.delete()
    return Response(f'{product} Deleted successfully')
