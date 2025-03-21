from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer
from main.models import Product, Review


@api_view(['GET'])
def products_list_view(request):
    Products = Product.objects.all()
    serializer = ProductListSerializer(Products, many=True)
    return Response(serializer.data)



class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(pk=product_id)
            serializer = ProductDetailsSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Товар не найден"}, status=404)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        mark_param = request.query_params.get('mark')
        queryset = Review.objects.filter(product_id=product_id)
        
        if mark_param is not None:
            try:
                mark_value = int(mark_param)
                queryset = queryset.filter(mark=mark_value)
            except ValueError:
                return Response({"error": "Параметр mark должен быть целым числом."}, status=400)
        
        queryset = queryset.order_by('mark')
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)
