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
        if not request.user.is_admin:
            return queryset.filter(house=request.user.tenant.house)
        else:
            queryset_from = queryset.filter(from_owner=True, house__in=request.user.house_set.all())
            queryset_to = queryset.filter(notify_owner=True, house__in=request.user.house_set.all())
            return queryset_from | queryset_to


# class LandlordFilter(BaseFilterBackend):
#     """
#     landlord only sees events concerning himself
#     """
#     def filter_queryset(self, request, queryset, view):
#         """
#
#         :param request:
#         :param queryset:
#         :param view:
#         :return:
#         """
#         if request.user.is_admin:
#             queryset_from = queryset.filter(from_owner=True)
#             queryset_to = queryset.filter(notify_owner=True)
#             return queryset_from | queryset_to
