import json
from django.http import JsonResponse
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods
from .models import Shoe, BinVO


class BinVOEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "closet_name",
        "bin_number",
    ]


class ShoeEncoder(ModelEncoder):
    model = Shoe
    properties = ["manufacturer",
                  "model_name",
                  "color",
                  "picture_url",
                  "shoe_bin",
                  ]
    encoders = {"shoe_bin": BinVOEncoder()}


@require_http_methods({"GET", "POST"})
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeEncoder
        )
    else:
        content = json.loads(request.body)
        try:
            bin_href = content['shoe_bin']
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
            encoder=ShoeEncoder,
            safe=False,
        )
