from django.shortcuts import render
from django.http import JsonResponse
from contacts_app.models import Account
from django.views.decorators.csrf import csrf_exempt
import json


def start_api(request):
    users = Account.objects.all()

    if users:
        data = [
            {
                "id": user.id,
                "created": user.created,
                "user": str(user.user),
                "firstname": user.firstname,
                "lastname": user.lastname,
                "email": user.email,
                "address": user.address,
                "phoneNumber": user.phoneNumber,
                "linkedin": user.linkedin,
                "facebook": user.facebook,
                "twitter": user.twitter,
            }
            for user in users
        ]

        return JsonResponse({"data": data}, safe=False)

    return JsonResponse({"error": "Object not found"}, status=404)


@csrf_exempt
def create_obj(request):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("firstname", "")

        # Validate and create the object
        new_obj = Account.objects.create(firstname=name)
        response_data = {"id": new_obj.id, "name": new_obj.name}
        return JsonResponse(response_data, status=201)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def update_obj(request, object_id):
    if request.method == "PUT":
        data = json.loads(request.body)
        name = data.get("firstname", "")
        try:
            obj = Account.objects.get(id=object_id)
            obj.firstname = name
            obj.save()
            response_data = {"id": obj.id, "name": obj.name}
            return JsonResponse(response_data)
        except Account.DoesNotExist:
            return JsonResponse({"error": "Object not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)


@csrf_exempt
def delete_obj(request, object_id):
    if request.method == "DELETE":
        try:
            obj = Account.objects.get(id=object_id)
            obj.delete()
            return JsonResponse({"message": "Object deleted successfully"})
        except Account.DoesNotExist:
            return JsonResponse({"error": "Object not found"}, status=404)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
