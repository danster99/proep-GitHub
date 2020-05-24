from rest_framework.filters import BaseFilterBackend


class CustomFilter(BaseFilterBackend):
    """
    filter that allows a user to only see the house they're part of
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


class LandlordFilter(BaseFilterBackend):
    """
    landlord only sees events concerning himself
    """
    def filter_queryset(self, request, queryset, view):
        """

        :param request:
        :param queryset:
        :param view:
        :return:
        """
        if request.user.is_admin:
            return queryset.filter(notify_owner=True)
