from http import HTTPStatus

from django.shortcuts import render


def not_found(request, *args):
    tempate = 'core/404.html'
    context = {
        'path': request.path,
        'host': request.get_host()
    }
    return render(request, tempate, context, status=HTTPStatus.NOT_FOUND)


def server_error(request, *args):
    template = 'core/500.html'
    return render(request, template, status=HTTPStatus.INTERNAL_SERVER_ERROR)
