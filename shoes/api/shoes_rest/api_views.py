import json
from django.http import JsonResponse
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods
from .models import Shoe, BinVO


class BinVOListEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "closet_name",
        "bin_number",
    ]


class BinVODetailEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "closet_name",
        "bin_number",
        "bin_size",
        "import_href",
    ]


class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "model_name",
        "color",
        "id",
    ]
    encoders = {"shoe_bin": BinVOListEncoder()}


class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "model_name",
        "color",
        "picture_url",
        "shoe_bin",
    ]
    encoders = {"shoe_bin": BinVODetailEncoder()}


@require_http_methods({"GET", "POST"})
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        return JsonResponse({"shoes": shoes}, encoder=ShoeListEncoder)
    else:
        content = json.loads(request.body)
        try:
            bin_href = content["shoe_bin"]
            bin = BinVO.objects.get(import_href=bin_href)
            content["shoe_bin"] = bin
        except BinVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid bin"},
                status=400,
            )

        shoe = Shoe.objects.create(**content)
        return JsonResponse(
            shoe,
            encoder=ShoeListEncoder,
            safe=False,
        )


@require_http_methods({"GET", "DELETE"})
def api_shoe_detail(request, id):
    if request.method == "GET":
        shoe = Shoe.objects.get(id=id)
        return JsonResponse(
            {"shoe": shoe},
            encoder=ShoeDetailEncoder
            )
    else:
        count, _ = Shoe.objects.filter(id=id).delete()
        return JsonResponse({"Deleted": count > 0})
