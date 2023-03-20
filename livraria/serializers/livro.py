from rest_framework.serializers import ModelSerializer
from livraria.models import Livro

class LivroSerializer(ModelSerializer):
    class Meta:
        model = Livro
        fields = "__all__"