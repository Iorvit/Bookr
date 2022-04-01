from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required


def greeting_view(request):
    user = request.user
    return HttpResponse("Hey, there welcome to Bookr! Your one stop place to review books.")


@login_required
def greeting_view_user(request):
    user = request.user 
    return HttpResponse("Hey {username}, welcome to Bookr!".format(username=user))
