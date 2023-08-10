from rest_framework import serializers
from .models import invoice, invoicedetail



class invoicedetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = invoicedetail
        # fields = ['description','quantity','unitprice','price']
        fields = ['description']



class invoiceSerializer(serializers.ModelSerializer):
    invoice_detail=invoicedetailSerializer(many=True)
    class Meta:
        model = invoice
        fields= ['invoice_detail','name']