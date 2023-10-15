from rest_framework.mixins import ListModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet


class ListUpdateViewSet(ListModelMixin, UpdateModelMixin, GenericViewSet):
    pass
