# -*- coding: utf-8 -*-

from rest_framework.viewsets import ReadOnlyModelViewSet
from api_v1 import models, serializers


class TagViewSet(ReadOnlyModelViewSet):
    queryset            = models.Tag.objects.all()
    serializer_class    = serializers.TagSerializer
