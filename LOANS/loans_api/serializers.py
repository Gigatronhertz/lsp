from rest_framework import serializers
from .models import *

class Loan_CategoriesSerializer(serializers.ModelSerializer):
    message=  serializers.CharField(max_length = 200)
    name =  serializers.CharField(max_length = 200)
    loan_category_id=  serializers.UUIDField()
    Id = models.UUIDField()
    updated_at= serializers.DateTimeField()
    created_at= serializers.DateTimeField()

    class Meta:
        model = Loan_Categories
        fields = ('__all__')

class Loan_TypeSerializer(serializers.ModelSerializer):

    message= serializers.CharField(max_length = 200)
    name =serializers.CharField(max_length = 200)
    loan_category_id = serializers.UUIDField()
    loan_type_id= serializers.UUIDField()
    updated_at =serializers.DateTimeField()
    created_at =serializers.DateTimeField()

    class Meta:
        model = Loan_Type
        fields = ('__all__')
    





class Loan_OffersSerializer (serializers.ModelSerializer):
    name =serializers.CharField(max_length = 200)
    minimum_amount = serializers.FloatField()
    maximum_amount =serializers.FloatField()
    minimum_duration =serializers.FloatField()
    loan_type_id =serializers.UUIDField()
    intrest_rate_value =serializers.FloatField()
    minimum_monthly_salary =serializers.FloatField()


    class Meta:
        model =Loan_Offers
        fields = ('__all__')

class Loan_ApplicationsSerializer(serializers.ModelSerializer):
    message = serializers.CharField(max_length = 200)
    Id  = serializers.UUIDField()
    applicant_id  = serializers.UUIDField()
    loan_offer_id  =serializers.UUIDField()
    amount_intended= serializers.FloatField()
    amount_received = serializers.FloatField()
    status = serializers.CharField(max_length = 200)
    approved_at = serializers.DateTimeField()
    declined_at = serializers.DateTimeField()
    created_at= serializers.DateTimeField()
    updated_at= serializers.DateTimeField()

    class Meta:
        model =Loan_Applications
        fields = ('__all__')




