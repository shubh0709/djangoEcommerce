from django.http import HttpResponse


def index(request):
    return HttpResponse("product page")


def createProduct(request):
    return HttpResponse("product page")


def uploadImage(request):
    return HttpResponse("product page")


def createProductReview(request):
    return HttpResponse("product page")


def getTopProducts(request):
    return HttpResponse("product page")


def getProducts(request):
    return HttpResponse("product page")


def getProduct(request):
    return HttpResponse("product page")


def updateProduct(request):
    return HttpResponse("product page")


def deleteProduct(request):
    return HttpResponse("product page")
