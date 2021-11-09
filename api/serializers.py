from rest_framework import serializers
from .models import Artical

# class ArticalSerializer(serializers.Serializer):
#   title = serializers.CharField(max_length=50)
#   description = serializers.CharField(max_length=50)
  
#   def create(self, validated_data):
#    return Artical.objects.create(validated_data)
#   def update(self, instance, validated_data):
#    instance.title = validated_data.get('title', instance.title)
#    instance.description = validated_data.get('description', instance.description)


class ArticalSerializer(serializers.ModelSerializer):
 class Meta:
  model = Artical
  fields = '__all__'