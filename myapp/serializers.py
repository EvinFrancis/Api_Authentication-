from myapp.models import User
from rest_framework import serializers
class User_Serializer(serializers.ModelSerializer):
    class Meta:

        # 🔹 Model this serializer is based on
        model=User
        # 🔹 Fields that will be accepted from request & shown in response
        fields=[
            "id","name","email","password"# password is write_only, so it won't be shown in response
        ]
        # 🔹 Extra configuration for fields///... extra_kwargs defines field rules for put ;...
        extra_kwargs={
            "name":{"required":False},
            "password":{"write_only":True} 
            # password:
            # - write_only=True → can be sent in request
            # - will NOT be returned in response (security)
        }
    

    def create(self, validated_data):#when create method is called, it receives validated_data which is a dict of the fields that passed validation (name, email, password)


        psw=validated_data.pop("password",None) #pop used to remove alrdy exist pswrd
#         ✔️ psw → plain password entered by user
# ❌ validated_data → no password anymore, only other fields like name and email



        instance=self.Meta.model(**validated_data)# create model instance with remaining validated data (without password)
        if psw is not None:
            instance.set_password(psw)# set_password hashes the password and stores it securely in the instance
        #Converts plain password → hashed password
        instance.save() # save the instance to database
        return instance
        