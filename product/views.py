"""
this file used for product viewset
"""
# Third part imports
from rest_framework.response import Response
from rest_framework import status

# Local imports
from .constant import ModelViewSet
from .models import Product
from .serializer import ProductSerializer, GetProductSerializer, EditProductSerializer


class ProductViewset(ModelViewSet):
    """
    create and list a product
    """
    http_method_names = ('get', 'post', 'put', 'delete')
    serializer_class = ProductSerializer
    queryset = Product

    def get_queryset(self):
        """
        fetching list from a database
        :return: list of queryset
        """
        product_obj = Product.objects.filter(is_active=True)
        return product_obj

    def create(self, request, *args, **kwargs):
        """
        to create a list
        :param request: wsgi request
        :param args: args
        :param kwargs: keyword extra argument
        :return: sucess message or error
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'data': 'Product Added Successfully!'
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'error': serializer.errors,
        })

    def list(self, request, *args, **kwargs):
        """
        list of product
        :param request: wsgi request
        :param args: args
        :param kwargs:key word extra argument
        :return: list instance
        """
        serializer = GetProductSerializer(self.get_queryset(), many=True).data
        if serializer:
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'data': serializer.errors
        })

    def retrieve(self, request, *args, **kwargs):
        """
        get product on id
        :param request:wsgi request
        :param args:args
        :param kwargs:kwargs
        :return:product instance
        """
        pk = kwargs['pk']
        instance = self.queryset.objects.get(id=pk)
        serializer = self.serializer_class(instance)
        if serializer:
            return Response({
                'status': status.HTTP_200_OK,
                'data': serializer.data
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'data': serializer.errors
        })

    def update(self, request, *args, **kwargs):
        """
        update a product
        :param request: wsgi request
        :param args: args
        :param kwargs: kwargs
        :return: success message or error
        """
        instance = Product.objects.get(id=kwargs['pk'])
        serializer = EditProductSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'data': 'Product Successfully updated'
            })
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'data': 'something went wrong'
        })

    def destroy(self, request, *args, **kwargs):
        """
        delete a product
        :param request: wsgi request
        :param args: args
        :param kwargs: kwargs
        :return: success message or error
        """
        instance = self.queryset.objects.get(id=kwargs['pk'])
        if instance:
            instance.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'data':'deleted successfully!'
            })

        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'data': 'something went wrong'
        })
