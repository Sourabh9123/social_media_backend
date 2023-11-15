from rest_framework.permissions import BasePermission
from django.urls import resolve

# class has_owner(BasePermission):
#     def has_permission(self, request, view):
#         resolved = resolve(request.path_info)
#         pk = resolved.split('/')
#         print(pk)
#         return True