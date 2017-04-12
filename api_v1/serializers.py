# -*- coding: utf-8 -*-

from rest_framework_json_api.serializers import ModelSerializer
from api_v1 import models


class TagSerializer(ModelSerializer):
    class Meta:
        model = models.Tag
        fields = [
            'name',
        ]
