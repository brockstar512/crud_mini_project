from rest_framework import serializers
from apps.api.models import (
Definition, Word
)

class DefinitionSerializer(serializers.ModelSerializer):

    #instance coming from the owner model. its read only. the owner cannot edit, only read.
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Definition #does this have to be in the same order as models or is this random or is this the order we view it in?

        # pass as a tupple. all the inputs in the classes of the corresponding serializers
        fields = ('id', 'definition',
                  'owner', 'word',
                  'part_of_speech', 'sentence',
                  'created_at', 'updated_at',
                  'is_public')


class WordSerializer(serializers.ModelSerializer):
    # this is call an instance
    # \/
    owner = serializers.ReadOnlyField(source='owner.username')
    # word can have many definitions ThIs Coresponds......
    definitions = DefinitionSerializer(many=True, read_only=True, required=False)#this cannot be read only and required

    class Meta:                     #.... with this
        model = Word  # this order does not matter. this is just the structure of your JSON?? does that mean views or models
        fields = ('id', 'name', 'owner', 'definitions', 'created_at',
                  'updated_at',)
