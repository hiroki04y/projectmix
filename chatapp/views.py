from django.shortcuts import render

# Create your views here.

print('chatapp通過')
def chatfunc(request):
    return render(request, 'chat.html')