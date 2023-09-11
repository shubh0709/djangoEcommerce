from django.http import HttpResponse


def index(request):
    return HttpResponse("product page")


def create(request):
    return HttpResponse("product page")


def upload(request):
    return HttpResponse("product page")


def createProductReview(request):
    return HttpResponse("product page")


def getTopProducts(request):
    return HttpResponse("product page")


def getProduct(request):
    return HttpResponse("product page")


def updateProduct(request):
    return HttpResponse("product page")


def deleteProduct(request):
    return HttpResponse("product page")
