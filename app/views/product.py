from django.http import HttpResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("product page")


def create_product(request):
    return HttpResponse("product page")


def upload_image(request):
    return HttpResponse("product page")


def create_product_review(request):
    return HttpResponse("product page")


def get_top_products(request:Request):
    return HttpResponse("product page")


@api_view(http_method_names=["GET"])
def get_products(request: Request):
    return HttpResponse("product page")


def get_product(request):
    return HttpResponse("product page")


def update_product(request):
    return HttpResponse("product page")


def delete_product(request):
    return HttpResponse("product page")
