from rest_framework.filters import BaseFilterBackend


class BookingFilter(BaseFilterBackend):
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
        new_queryset = queryset.filter(room__house=request.user.tenant.house)
        second = queryset.filter(utility__house=request.user.tenant.house)
        return new_queryset | second

