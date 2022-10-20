from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings
from core.models import *


# Create your views here.


@login_required(login_url="/sign-in/?next=/courier/")
def home(request):
    return redirect(reverse('courier:available_jobs'))


@login_required(login_url="/sign-in/?next=/courier/")
def available_jobs_page(request):
    return render(request, 'courier/available_jobs.html', {
        "GOOGLE_MAP_API_KEY": settings.GOOGLE_MAP_API_KEY,
    })

@login_required(login_url="/sign-in/?next=/courier/")
def available_job_page(request, id): 
    job = Job.objects.filter(id=id, status = Job.PROCESSING_STATUS).last()

    if not job:
        return redirect(reverse('courier:available_jobs'))

    if request.method == "POST":
        job.courier = request.user.courier
        job.status = Job.PICKING_STATUS
        job.save()

        return redirect(reverse('courier:available_jobs'))

    # if request.method == "POST":
    #     job.courier = request.user.courier
    #     job.status = Job.PICKING_STATUS
    #     job.save()

    #     try:
    #         layer = get_channel_layer()
    #         async_to_sync(layer.group_send)("job_" + str(job.id), {
    #             'type': 'job_update',
    #             'job': {
    #                 'status': job.get_status_display(),
    #             }
    #         })
    #     except:
    #         pass

    #     return redirect(reverse('courier:available_jobs'))

    return render(request, 'courier/available_job.html', {
        "job": job,
    })
