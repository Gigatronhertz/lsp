from django.urls import path
from .views import *
from .models import *

urlpatterns = [ 


    path('loan-categories', Loan_CategoriesViews.as_view()),
    path('loan-types', Loan_TypeViews.as_view()),
    path('loan-offers', Loan_OffersViews.as_view()),
    path('loan-offers/<loan_type_id>', Loan_OffersViews.as_view()),
    path('loan-applications/<Id>/respond', Loan_ApplicationsViews.as_view()),
    path('loan-applications/respond', Loan_ApplicationsViews.as_view()),

]


