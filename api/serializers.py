from rest_framework.serializers import ModelSerializer

from .models import Product, Order, Discount


class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = "__all__"


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    discounts = DiscountSerializer(read_only=True, many=True)


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
