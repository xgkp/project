from django.shortcuts import render, HttpResponse

# Create your views here.
def movie_list(request):
    return HttpResponse(f"电影的列表")

def movie_detail(request, movie_id):
    return HttpResponse(f"电影详情:{movie_id}")