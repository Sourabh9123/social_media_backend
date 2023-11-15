from storeapp.models import Product,  Category
from rest_framework.serializers import ModelSerializer



class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"