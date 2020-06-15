from rest_framework.filters import BaseFilterBackend


class UtilityFilter(BaseFilterBackend):
    """
    filter that allows a user to only see the utilities from the house they're
    a part of
    """
    def filter_queryset(self, request, queryset, view):
        """
        returns filtered queryset
        :param request:
        :param queryset:
        :param view:
        :return:
        """

        return queryset.filter(house=request.user.tenant.house)