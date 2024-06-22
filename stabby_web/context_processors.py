def collectors_group(request):
    if request.user.is_authenticated:
        is_collector = request.user.groups.filter(name="Collectors").exists()
    else:
        is_collector = False
    return {"is_collector": is_collector}
