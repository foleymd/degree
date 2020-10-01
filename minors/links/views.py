from django.shortcuts import render_to_response

from utdirect.templates import UTDirectContext

from degree.minors.utd_defaults import PROJECT_UTD_DEFAULTS

defaults = PROJECT_UTD_DEFAULTS


def index(request):

    context = {}

    return render_to_response("links.html", UTDirectContext(request, context, defaults=defaults))
