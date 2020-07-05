from .models import Department, Banner


def all_departments(request):
    departments = Department.objects.values("department")
    return {"departments": departments}


# def banner(request):
#     new_banner = Banner.objects.last()
#     return {"new_banner": new_banner}
