from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    role = request.user.role

    if role == 'WEB':
        return redirect('/admin/')
    elif role == 'CONV':
        return redirect('/forms/')
    elif role == 'SIG':
        return redirect('/forms/')
    else:
        return render(request, 'accounts/general.html')
