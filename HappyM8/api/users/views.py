from django.shortcuts import render
from django.views.generic import View
from HappyM8.users.forms import UserForm
# Create your views here.


class UserView(View):

    def get(self, request, *args, **kwargs):
        return self.render(
            request, context={
                'form': UserForm
            })
