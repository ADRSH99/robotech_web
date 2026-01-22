from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .models import Response
from forms_app.models import Form


@login_required
def response_list(request, form_id):
    if request.user.role not in ['WEB', 'CONV', 'SIG']:
        return HttpResponseForbidden("Access denied")

    form = get_object_or_404(Form, id=form_id)
    responses = Response.objects.filter(form=form)

    return render(
        request,
        'responses/response_list.html',
        {'form': form, 'responses': responses}
    )


@login_required
def edit_response(request, response_id):
    if request.user.role not in ['WEB', 'CONV']:
        return HttpResponseForbidden("Access denied")

    response = get_object_or_404(Response, id=response_id)

    if request.method == 'POST':
        response.answers = dict(request.POST)
        response.save()

    return render(
        request,
        'responses/edit_response.html',
        {'response': response}
    )
