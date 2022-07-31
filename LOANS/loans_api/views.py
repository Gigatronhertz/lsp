from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

class Loan_CategoriesViews(APIView):

     def get (self, request):
        serializer = Loan_CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class Loan_TypeViews(APIView):

     def post(self, request):
        serializer = Loan_TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




class Loan_OffersViews(APIView):

     def post(self, request):
        serializer = Loan_OffersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



     def get(self, request, loan_type_id ):
        
        if loan_type_id:
            loan =Loan_Offers.objects.get( loan_type_id= loan_type_id)
            serializer = Loan_OffersSerializer(loan)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        loans = Loan_Offers.objects.all()
        serializer = Loan_OffersSerializer(loans, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)



     def put(self, request, loan_type_id):
        serializer = Loan_OffersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

 
     def delete(self, request, loan_type_id):
       loan = Loan_Offers.objects.filter( loan_type_id= loan_type_id)
       if loan:
            loan.delete()
            return Response({"status": "success", "data": " Loan_Offers Deleted"})



class Loan_ApplicationsViews(APIView):
    def put (self, request, loan_type_id):
        serializer = Loan_ApplicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, loan_type_id ):
        
        if loan_type_id:
            applications =Loan_Applications.objects.get( loan_type_id= loan_type_id)
            serializer = Loan_ApplicationsSerializer(applications)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        applications = Loan_Applications.objects.all()
        serializer = Loan_OffersSerializer(applications, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)



