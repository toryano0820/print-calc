import json

from rest_framework.views import APIView
from rest_framework.request import HttpRequest
from rest_framework.response import Response
from rest_framework import permissions, status

from .models import Product, Discount
from .serializers import ProductSerializer, DiscountSerializer


class ProductAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        serializer = ProductSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request: HttpRequest):
        data = json.loads(request.body)
        product_id = data.get("id")
        discounts = data.get("discounts")

        product = Product.objects.get(id=product_id)
        discounts = Discount.objects.filter(id__in=discounts)
        for discount in discounts:
            print(discount)
            product.discounts.add(discount)

        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class DiscountAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request: HttpRequest):
        discounts = Discount.objects.all()
        serializer = DiscountSerializer(discounts, many=True)
        return Response(serializer.data)

    def post(self, request: HttpRequest):
        data = json.loads(request.body)
        serializer = DiscountSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
