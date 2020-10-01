from django.shortcuts import render_to_response
from utdirect.templates import UTDirectContext
from degree.minors.utd_defaults import PROJECT_UTD_DEFAULTS

defaults = PROJECT_UTD_DEFAULTS

def index(request):

    context = UTDirectContext(request, {}, defaults=defaults, access_context='P', document_title='Important Minor and Certificate Links for Students')

    return render_to_response("student_links/student_links.html", context)