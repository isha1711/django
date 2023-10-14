from rest_framework import serializers
from.models import prodmodel
class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = prodmodel
		fields='__all__'