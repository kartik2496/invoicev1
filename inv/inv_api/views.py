from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import invoice
from .serializers import invoiceSerializer
from rest_framework import serializers, viewsets
from rest_framework import status
from rest_framework.parsers import JSONParser


# @api_view(['GET'])
# def ApiOverview(request):
#     api_urls = {
#         'all_items': '/',
#         'Add': '/create',
#     }

#     return Response(api_urls)



# @api_view(['POST'])
# def add_items(request):
#     item = invoiceSerializer(data=request.data)

#     # validating for already existing data
#     if invoice.objects.filter(**request.data).exists():
#         raise serializers.ValidationError('This data already exists')

#     if item.is_valid():
#         item.save()
#         return Response(item.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)




# @api_view(['GET'])
# def view_items(request):
     
     
#     # checking for the parameters from the URL
#     if request.query_params:
#         items = invoice.objects.filter(**request.query_params.dict())
#     else:
#         items = invoice.objects.all()
 
#     # if there is something in items else raise error
#     if items:
#         serializer = invoiceSerializer(items, many=True)
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)



class invoiceModelViewSet(viewsets.ModelViewSet):
    queryset = invoice.objects.all()
    serializer_class = invoiceSerializer
    parser_classes = (JSONParser,)

