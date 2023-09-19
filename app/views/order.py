from datetime import datetime

from app.models import Order, OrderItem, Product, ShippingAddress
from app.serializers import OrderSerializer, ProductSerializer
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(http_method_names=['GET'])
def index(request: Request, response: Response):
    return response("order page")


def getOrders(request: Request, response: Response):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


def addOrderItems(request: Request, response: Response):
    return HttpResponse("order page")


def getMyOrders(request: Request, response: Response):
    return HttpResponse("order page")


def updateOrderToDelivered(request: Request, response: Response):
    return HttpResponse("order page")


def getOrderById(request: Request, response: Response):
    return HttpResponse("order page")


def updateOrderToPaid(request: Request, response: Response):
    return HttpResponse("order page")
