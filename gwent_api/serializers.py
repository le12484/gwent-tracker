from rest_framework import serializers
from models import Card, Category, Rarity, Group, Faction, Position, Variation, CardSet


class CardSetSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)


class FactionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)

    def create(self, validated_data):
        """
        Create and return a new `group` instance, given the validated data.
        """
        return Faction.objects.create(**validated_data)


class GroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `group` instance, given the validated data.
        """
        return Group.objects.create(**validated_data)


class RaritySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `rarity` instance, given the validated data.
        """
        return Rarity.objects.create(**validated_data)


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `category` instance, given the validated data.
        """
        return Category.objects.create(**validated_data)


class PositionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)

    def create(self, validated_data):
        """
        Create and return a new `position` instance, given the validated data.
        """
        return Position.objects.create(**validated_data)


class VariationSerializer(serializers.Serializer):
    availability = serializers.CharField(max_length=200)
    rarity = serializers.CharField(max_length=200)


class CardSerializer(serializers.Serializer):
    categories = CategorySerializer(many=True)
    flavor = serializers.CharField(max_length=1200)
    info = serializers.CharField(max_length=1200)
    name = serializers.CharField(max_length=200)
    faction = FactionSerializer(many=False)
    group = GroupSerializer(many=False)
    rarity = RaritySerializer(many=False)
    art = serializers.CharField(max_length=1200)
    positions = PositionSerializer(many=True)
    availability = CardSetSerializer(many=False)

    def create(self, validated_data):
        """
        Create and return a new `Card` instance, given the validated data.
        """
        #request = self.context['request']
        faction_data = validated_data.pop('faction', None)
        if faction_data:
            faction = Faction.objects.get_or_create(**faction_data)[0]
            validated_data['faction'] = faction

        group_data = validated_data.pop('group', None)
        if group_data:
            group = Group.objects.get_or_create(**group_data)[0]
            validated_data['group'] = group

        rarity_data = validated_data.pop('rarity', None)
        if rarity_data:
            rarity = Rarity.objects.get_or_create(**rarity_data)[0]
            validated_data['rarity'] = rarity
        
        avail_data = validated_data.pop('availability', None)
        if avail_data:
            availability= CardSet.objects.get_or_create(**avail_data)[0]
            validated_data['availability'] = availability

        categories_data = validated_data.pop('categories')
        positions_data = validated_data.pop('positions')

        card = Card.objects.create(**validated_data)

        
        for category in categories_data:
            cat = Category.objects.get_or_create(**category)[0]
            card.categories.add(cat)


        for position in positions_data:
            pos = Position.objects.get_or_create(**position)[0]
            card.positions.add(pos)

        return card
    # class Meta:
    #  model = Card


class CardListSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='card-detail',
        lookup_field='pk'
    )

    name = serializers.CharField(max_length=200)
