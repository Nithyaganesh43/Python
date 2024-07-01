from django.urls import path
 
# importing views from views..py
from view import GeeksList
urlpatterns = [
    path('', GeeksList.as_view()),
]