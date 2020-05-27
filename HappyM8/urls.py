"""HappyM8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from rest_framework import routers

from api.houses.views import HouseList, RoomList, CalendarList
from api.bookings.views import BookingList
from api.users.views import UserList, TenantList
from api.utilities.views import UtilityList
from api.chores.views import ChoreList, NewChoreList
from api.custom_events.views import CustomEventList
from api.notifications.views import NotificationList

endpoints = [
    (r'houses', HouseList, 'houses'),
    (r'users', UserList, None),
    (r'bookings', BookingList, None),
    (r'utilities', UtilityList, None),
    (r'chores', ChoreList, 'chore'),
    (r'customEvents', CustomEventList, None),
    (r'tenants', TenantList, 'tenants'),
    (r'rooms', RoomList, None),
    (r'newchore', NewChoreList, 'new-chore'),
    (r'notifications', NotificationList, None),
    (r'calendar', CalendarList, 'calendar')
]

router = routers.DefaultRouter()

for prefix, viewset, basename in endpoints:
    router.register(prefix=prefix, viewset=viewset, basename=basename)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'api/', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
