from django.urls import path
from . import views

app_name = 'homeapp'
urlpatterns = [
    # homeというURLが呼び出されたらhomefuncを呼び出す
    path('home/', views.HomeView.as_view(), name='home'),
    path('inquiry/', views.InquiryView.as_view(), name='inquiry'),
]