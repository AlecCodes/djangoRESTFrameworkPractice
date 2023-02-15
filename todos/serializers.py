from .models import Todo
from rest_framework import serializers

#custom serializer so we only get those three fields in our model
class TodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # which model will get serialized
        model = Todo
        # which fields should be included in output
        fields = ['id','subject','details']