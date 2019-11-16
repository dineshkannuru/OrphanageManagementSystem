from rest_framework import serializers
from homepage.models import donatemoney,donatevaluables,Orphanage
from django.contrib.auth.models import User

class MoneySerializer(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField('get_userid')

    class Meta:
        model = donatemoney
        fields = ("__all__")
    
    def get_userid(self,donatemoney):
        user_id = donatemoney.user_id
        return user_id



class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'id')

class testdonatemoneyserializer(serializers.ModelSerializer):
    class Meta:
        model = donatemoney
        fields = ('__all__')

class testorphanageserializer(serializers.ModelSerializer):
    class Meta:
        model = Orphanage
        fields = ('__all__')
        