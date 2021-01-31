from django.shortcuts import redirect


def is_user_authenticated(view_function):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/chat/')
        else:
            return view_function(request, *args, **kwargs)
    return wrapper