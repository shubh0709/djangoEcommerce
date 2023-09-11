from django.http import HttpResponse


def index(request):
    return HttpResponse("order page")


def getOrders(request):
    return HttpResponse("order page")


def addOrderItems(request):
    return HttpResponse("order page")


def getMyOrders(request):
    return HttpResponse("order page")


def updateOrderToDelivered(request):
    return HttpResponse("order page")


def getOrderById(request):
    return HttpResponse("order page")


def updateOrderToPaid(request):
    return HttpResponse("order page")
