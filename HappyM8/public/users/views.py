from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from public.users.forms import UserForm
# Create your views here.


class UserView(View):

    def get(self, request, *args, **kwargs):
        return self.render(
            request, context={
                'form': UserForm
            })
