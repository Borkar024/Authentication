from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email')
        
        def create(self, Validate_data):
            obj = User.objects.create.user(**Validate_data)
            return obj
        