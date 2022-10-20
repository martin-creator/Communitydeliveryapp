from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from core.models import *
from django.utils import timezone

@csrf_exempt # it means this page is safe, you dont need to check the csrf
@login_required(login_url="/courier/sign-in/")
def available_jobs_api(request):
    # jobs = Job.objects.filter(status=Job.PROCESSING_STATUS)  # This will return query set
    jobs = list(Job.objects.filter(status=Job.PROCESSING_STATUS).values())

    return JsonResponse({
        "success": True,
        "jobs": jobs,
    })
