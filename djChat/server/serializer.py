from rest_framework import serializers

from .models import Server, Channel

class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = '__all__'

class ServerSerializer(serializers.ModelSerializer):

    num_members = serializers.SerializerMethodField(method_name='get_num_members')
    channel_server = ChannelSerializer(many=True)
    class Meta:
        model = Server
        exclude = ('member', )

    def get_num_members(self, obj):
        if hasattr(obj, "num_members"):
            return obj.num_members
        return None
    
    def to_representation(self, instance):
        data = super().to_representation(instance)      # super() calls the parent class without specifying parent class name.
        num_members = self.context.get("num_members")
        if not num_members:
            # here None is the default returned if num_members is not found.
            data.pop("num_members", None)         # if no data pop will remove num_members field
        return data
