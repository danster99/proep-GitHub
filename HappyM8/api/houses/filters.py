from rest_framework.filters import BaseFilterBackend


class IsOwnerFilter(BaseFilterBackend):
    """
    filter that allows a user to only see the house created by them
    """
    def filter_queryset(self, request, queryset, view):
        """
        returns filtered queryset
        :param request:
        :param queryset:
        :param view:
        :return:
        """
        return queryset.get(owner=request.user)