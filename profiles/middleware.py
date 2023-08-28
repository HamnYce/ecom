from rest_framework import permissions
from django.http import JsonResponse
from django.middleware.http import ConditionalGetMiddleware
from django.http.request import HttpRequest

import rest_framework.status as status


class ProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        path = request.get_full_path()

        profile_creation_path = '/profiles/all/'
        authentication_base = 'auth'
        if ('/profiles/all/' == path[:len(profile_creation_path)] or
            authentication_base == path.split('/')[1]
            ):
            return response

        if (request.method not in permissions.SAFE_METHODS and
                not request.user.has_profile):
            return JsonResponse(
                {'reason': 'please create a profile first'},
                status=status.HTTP_400_BAD_REQUEST
            )

        return response
