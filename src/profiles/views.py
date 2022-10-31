from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import PhDStudentProfileModel, StaffProfileModel


def staff_list(request):
    object_split = 8
    staffs_list = StaffProfileModel.objects.order_by("name")
    paginator = Paginator(staffs_list, object_split)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    page_range = paginator.page_range
    return render(request, "staff/staff_list.html", {"objects": page_obj, "page_range": page_range})


def staff_full(request, slug):
    staff = StaffProfileModel.objects.filter(slug=slug).first()
    if not staff:
        return HttpResponseNotFound()
    return render(request, "staff/staff_full.html", {"staff": staff})


def phd_list(request):
    object_split = 8
    phds_list = PhDStudentProfileModel.objects.order_by("name")
    paginator = Paginator(phds_list, object_split)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    page_range = paginator.page_range
    return render(request, "phd/phd_list.html", {"objects": page_obj, "page_range": page_range})


def phd_full(request, slug):
    phd_student = PhDStudentProfileModel.objects.filter(slug=slug).first()
    if not phd_student:
        return HttpResponseNotFound()
    return render(request, "phd/phd_full.html", {"phd": phd_student})
