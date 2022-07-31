from django.db import models

class   Loan_Categories(models.Model):
    message= models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    loan_category_id= models.UUIDField()
    updated_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Loan_Type(models.Model):

    message= models.CharField(max_length = 200)
    name = models.CharField(max_length = 200)
    loan_category_id = models.UUIDField()
    loan_categories = models.ForeignKey(Loan_Categories, on_delete = models.CASCADE)
    loan_type_id= models.UUIDField()
    updated_at =models.DateTimeField(auto_now_add=True)
    created_at =models.DateTimeField(auto_now_add=True)


class Loan_Offers (models.Model):
    name = models.CharField(max_length = 200)
    minimum_amount = models.FloatField()
    maximum_amount = models.FloatField()
    minimum_duration =models.FloatField()
    loan_type_id = models.UUIDField()
    intrest_rate_value =models.FloatField()
    minimum_monthly_salary = models.FloatField()
    Type = models.ForeignKey(Loan_Type, on_delete = models.CASCADE)


class Loan_Applications(models.Model):
    message = models.CharField(max_length = 200)
    Id  = models.UUIDField()
    applicant_id  = models.UUIDField()
    loan_offer_id  = models.UUIDField()
    amount_intended= models.FloatField()
    amount_received = models.FloatField()
    status = models.CharField(max_length = 200)
    approved_at = models.DateTimeField(auto_now_add=True)
    declined_at = models.DateTimeField(auto_now_add=True)
    created_at =models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    loan_offers = models.ForeignKey(Loan_Offers, on_delete = models.CASCADE)

   




