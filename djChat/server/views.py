from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from django.db.models import Count

from .models import Server
from .serializer import ServerSerializer

class ServerListViewSet(viewsets.ViewSet):
    queryset = Server.objects.all()

    def list(self, request):
        category = request.query_params.get("category")
        qty = request.query_params.get("qty")
        by_user = request.query_params.get("by_user") == "true"     # to get current user
        by_serverid = request.query_params.get("by_serverid")
        with_num_members = request.query_params.get("with_num_members") == "true"
        
        if by_user or by_serverid and not request.user.is_authenticated:    # check user is loged
            raise AuthenticationFailed()
        
        if category:
            self.queryset = self.queryset.filter(category__name = category)
        
        if by_user:                 # to show current user matching in member
            user_id = request.user.id
            self.queryset = self.queryset.filter(member=user_id)
        
        if with_num_members:
            self.queryset = self.queryset.annotate(num_members=Count("member"))
        
        if qty:                     # to show num of items
            self.queryset = self.queryset[: int(qty)]
        
        if by_serverid:
            try:
                self.queryset = self.queryset.filter(id=by_serverid)
                if not self.queryset:
                    raise ValidationError(detail=f"Server with id {by_serverid} not found.")
            except ValueError:
                raise ValidationError(detail="Server value error")

        serializer = ServerSerializer(self.queryset, many=True, context={'num_members':with_num_members})
        return Response(serializer.data)
    
