from .serializers import PincodeSerializer

from .models import Pincode

from rest_framework.decorators import api_view

from rest_framework.response import Response


from rest_framework import status



@api_view(['GET'])
def pincode_details(request , pincode):
    try:
        pincode_obj = Pincode.objects.get(pincode = pincode)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    if request.method == 'GET':
        serializer = PincodeSerializer(pincode_obj)
        return Response({"city": serializer.data["city"] , "district": serializer.data["district"]} , status=status.HTTP_200_OK)
    
    else:
        pass



    







