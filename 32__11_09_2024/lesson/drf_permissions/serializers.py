from .models import User, Game, Type, Option, PaymentHistory, Item, Lot
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True, max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user



class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class OptionsSerializer(serializers.ModelSerializer):



    class Meta:
        model = Option
        fields = '__all__'

class TypesSerializer(serializers.ModelSerializer):

    options = OptionsSerializer(many=True)
    class Meta:
        model = Type
        fields = '__all__'



class GameInfoSerializer(serializers.ModelSerializer):

    types = TypesSerializer(many=True)


    class Meta:
        model = Game
        fields = '__all__'


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = '__all__'

        read_only_fields = ['id', 'type', 'created_at', 'user']


    def create(self, validated_data, *args, **kwargs):
        return PaymentHistory.objects.create(
            user=self.context.get('request').user,
            type='add',
            **validated_data
        )

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        depth = 3




class ProfileSerializer(serializers.ModelSerializer):

    items = ItemSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'balance', 'items']
        read_only_fields = ['id']



class LotsSerializer(serializers.ModelSerializer):

    item = ItemSerializer()
    count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Lot
        fields = '__all__'
        # depth = 1
