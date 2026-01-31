from myapp.models import User
from rest_framework import serializers
class User_Serializer(serializers.ModelSerializer):
    class Meta:
        # 🔹 Model this serializer is based on
        model=User
        # 🔹 Fields that will be accepted from request & shown in response
        fields=[
            "id","name","email","password"
        ]
        # 🔹 Extra configuration for fields///... extra_kwargs defines field rules for put ;...
        extra_kwargs={
            "name":{"required":False},
            "password":{"write_only":True} 
            # password:
            # - write_only=True → can be sent in request
            # - will NOT be returned in response (security)
        }