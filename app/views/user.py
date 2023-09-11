from django.http import HttpResponse


def index(request):
    return HttpResponse("user page")

def registerUser(request):
    return HttpResponse("user page")

def getUserProfile(request):
    return HttpResponse("user page")

def updateUserProfile(request):
    return HttpResponse("user page")

def getUsers(request):
    return HttpResponse("user page")

def getUserById(request):
    return HttpResponse("user page")

def updateUser(request):
    return HttpResponse("user page")

def deleteUser(request):
    return HttpResponse("user page")