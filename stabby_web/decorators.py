from functools import wraps


def skip_save(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the logged-in user is in the "Collectors" group
        is_collector = False
        if request.user.is_authenticated:
            is_collector = request.user.groups.filter(name="Collectors").exists()

        # Attach the `is_collector` flag to the request object
        request.is_collector = is_collector

        return view_func(request, *args, **kwargs)

    return _wrapped_view
