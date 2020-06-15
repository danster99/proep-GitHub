from rest_framework.filters import BaseFilterBackend


class ChoreFilter(BaseFilterBackend):
    """
    filter that allows a user to only access chores belonging to the house
    they're part of
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