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
from django.urls import path, include
from rest_framework import routers

from api.houses.views import HouseList, RoomList
from api.bookings.views import BookingList
from api.users.views import UserList, TenantList
from api.utilities.views import UtilityList
from api.chores.views import ChoreList
from api.custom_events.views import CustomEventList

endpoints = [
    (r'houses', HouseList),
    (r'users', UserList),
    (r'bookings', BookingList),
    (r'utilities', UtilityList),
    (r'chores', ChoreList),
    (r'customEvents', CustomEventList),
    (r'tenants', TenantList),
    (r'rooms', RoomList)
]

router = routers.DefaultRouter()

for prefix, viewset in endpoints:
    router.register(prefix=prefix, viewset=viewset)

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'api/', include(router.urls)),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]
