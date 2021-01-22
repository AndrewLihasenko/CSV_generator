from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import LoginForm


def user_login(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        login_form = LoginForm(request.POST)
        # check whether it's valid:
        if login_form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        login_form = LoginForm()

    return render(request, 'login.html', {'form': login_form})
