from django.urls import path
from .views import chatfunc

app_name = 'chatapp'
urlpatterns = [
    # homeというURLが呼び出されたらhomefuncを呼び出す
    path('chat/', chatfunc, name='chat'),
]