from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
from common.json import ModelEncoder
from .models import Hat, LocationVO

class LocationVOEncoder(ModelEncoder):
    model = LocationVO
    properties = [
        "import_href",
        "closet_name",
        "section_number",
        "shelf_number",
    ]

class HatEncoder(ModelEncoder):
    model = Hat
    properties = [
        "id",
        "fabric",
        "style_name",
        "color",
        "picture_url",
        "location",
    ]
    encoders = {
        "location": LocationVOEncoder(),
    }


@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    if request.method == "GET":
        hats = Hat.objects.all()
        return JsonResponse(
            {"hats": hats},
            encoder=HatEncoder,
        )
    else:
        content = json.loads(request.body)

        try:
            location = LocationVO.objects.get(id=content["location"])
            content["location"] = location
        except LocationVO.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid location id"},
                status=400,
            )

        hat = Hat.objects.create(**content)
        return JsonResponse(
            hat,
            encoder= HatEncoder,
            safe=False,
        )

@require_http_methods(["GET", "DELETE"])
def api_show_hats(request, id):
    if request.method == "GET":
        hat = Hat.objects.get(id=id)
        return JsonResponse(
            hat,
            encoder= HatEncoder,
            safe=False,
        )
    else:
        count, _ = Hat.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
