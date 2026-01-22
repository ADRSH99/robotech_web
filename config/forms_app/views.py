from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

from .models import Form
from responses.models import Response


# ---------- HELPERS ----------

def is_convener_or_above(user):
    return user.is_authenticated and user.role in ['WEB', 'CONV']


def is_sig_or_above(user):
    return user.is_authenticated and user.role in ['WEB', 'CONV', 'SIG']


# ---------- VIEWS ----------

@login_required
def form_list(request):
    if not is_sig_or_above(request.user):
        return HttpResponseForbidden("Access denied")

    forms = Form.objects.all()
    return render(request, 'forms/form_list.html', {'forms': forms})


@login_required
def create_form(request):
    if not is_convener_or_above(request.user):
        return HttpResponseForbidden("Access denied")

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Form.objects.create(
            title=title,
            description=description
        )
        return redirect('form_list')

    return render(request, 'forms/create_form.html')


def public_form(request, public_id):
    form = get_object_or_404(Form, public_id=public_id, is_active=True)

    if request.method == 'POST':
        Response.objects.create(
            form=form,
            answers=dict(request.POST)
        )
        return render(request, 'forms/success.html')

    return render(request, 'forms/public_form.html', {'form': form})
