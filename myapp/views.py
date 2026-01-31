from django.shortcuts import render
from rest_framework.views import APIView
from myapp.models import User
from myapp.serializers import User_Serializer
from rest_framework.response import Response
from rest_framework import status

#obj contains:
# obj.initial_data → request data (dict)

# obj.fields → serializer field objects

# obj._errors → empty (initially)

# obj._validated_data → not created yet
# Create your views here.
class Registrations(APIView):
    def post(self,request):
        
        #this is////////////  ....... DESERIALIZATION...///////
        obj=User_Serializer(data=request.data)
        print(request.data)
        obj.is_valid(raise_exception=True)
        print(obj)      
        obj.save()
        return Response({"New user:":obj.data},status=status.HTTP_200_OK)
    
#     JSON (request)
#    ↓
# Python dict (request.data)
#    ↓
# Serializer  ←  THIS LINE
#    ↓
# validated_data
#    ↓
# Model object

#///////////////#this line is............ SERIALIZATION./...........//////////////
    
    def get(self, request):
        use=User.objects.all()
        print(use)
        obj=User_Serializer(use, many=True)#this line is SERIALIZATION.
        print(obj)
        return Response(obj.data,status.HTTP_200_OK)
    
#  Database
#    ↓
# User model objects (QuerySet)
#    ↓
# User_Serializer(use, many=True)
#    ↓
# Python list of dicts (obj.data)
#    ↓
# JSON response
    def put(self,request):
        data1=request.data
        try:
         obj=User.objects.get(id=data1["id"])
        except User.DoesNotExist:
            return Response("data not exist....",status=status.HTTP_400_BAD_REQUEST)
    
    
        use=User_Serializer(obj,data=data1)
     
        use.is_valid(raise_exception=True)
        use.save()
        return Response("updated succesfully...",status.HTTP_200_OK)
    

    def patch(self,request):
        data1=request.data
        try:
         obj=User.objects.get(id=data1["id"])
        except User.DoesNotExist:
            return Response("data not exist....",status=status.HTTP_400_BAD_REQUEST)
    
    
        use=User_Serializer(obj,data=data1,partial=True)#PATCH works because of partial=True,
        #....not because of extra_kwargs.
     
        use.is_valid(raise_exception=True)
        use.save()
        return Response("updated partial succesfully...",status.HTTP_200_OK)
    

    def delete(self,request,idd):
       try:
          
            obj=User.objects.get(id=idd)#Never use a variable outside try if it may not be assigned inside try
       except User.DoesNotExist:
          return Response("user db not found" ,status.HTTP_404_NOT_FOUND)
       
       obj.delete()
       return Response("Data Deleted sueccessfully...",status=status.HTTP_200_OK)
       
          
    

    
    


