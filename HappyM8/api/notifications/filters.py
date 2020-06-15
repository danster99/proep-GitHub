from rest_framework.filters import BaseFilterBackend


class NotificationFilter(BaseFilterBackend):
    """
    filter that allows a user to only see the notifications created by them.
    this filter is not used by landlords.
    """
    def filter_queryset(self, request, queryset, view):
        """
        returns filtered queryset
        :param request:
        :param queryset:
        :param view:
        :return:
        """
        if not request.user.is_admin:
            return queryset.filter(house=request.user.tenant.house)