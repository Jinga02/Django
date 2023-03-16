from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def throw(request):
    return render(request, 'articles/throw.html'
    )

def catch(request):
    # message를 받을건데 request 안쪽에 GET방식에 들어있는 데이터중에서 get해
    message = request.GET.get('message') 
    # print(message)
    context={
        'message' : message
    }
    return render(request, 'articles/catch.html', context)