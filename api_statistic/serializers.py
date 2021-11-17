from rest_framework import serializers
from .models import Case


class CaseSerializer(serializers.ModelSerializer):
    cpc = serializers.SerializerMethodField()
    cpm = serializers.SerializerMethodField()

    class Meta:
        model = Case
        fields = ("date", "views", "clics", "cost", "cpc", "cpm")

    def get_cpc(self, obj):
        if obj.cost is None or obj.clics is None:
            return None
        return obj.cost / obj.clics

    def get_cpm(self, obj):
        if obj.cost is None or obj.views is None:
            return None
        return obj.cost / obj.views * 1000
