from enum import Enum
from itertools import chain

from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

from events.models import EventModel
from news.models import NewsModel
from profiles.models import PhDStudentProfileModel, StaffProfileModel
from projects.models import Project


class SelectorEnum(Enum):
    EVERYTHING = "everything"
    NEWS = "news"
    PROJECTS = "projects"
    PHD = "phd_students"
    EVENTS = "events"
    STAFF = "staff"


def pagination(obj_list, obj_split, page):
    p = Paginator(obj_list, obj_split)
    obj = p.get_page(page)
    page_range = p.page_range
    return obj, page_range


def news_filter(searched):
    news_list = NewsModel.objects.filter(
        Q(title__icontains=searched) | Q(subtitle__icontains=searched) | Q(body__icontains=searched)
    ).order_by("-created_at")
    return news_list


def staff_filter(searched):
    staff_list = StaffProfileModel.objects.filter(Q(name__icontains=searched) | Q(biography__icontains=searched))
    return staff_list


def event_filter(searched):
    event_list = EventModel.objects.filter(Q(title__icontains=searched) | Q(body__icontains=searched)).order_by(
        "-created_at"
    )
    return event_list


def project_filter(searched):
    project_list = Project.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
    return project_list


def phd_filter(searched):
    phd_list = PhDStudentProfileModel.objects.filter(Q(name__icontains=searched) | Q(biography__icontains=searched))
    return phd_list


def search(request):
    page = request.GET.get("page")
    obj_split = 5  # numbers of items displaying in each page

    if request.method != "GET":
        return HttpResponse(status=405)

    selected = request.GET.get("selected", "everything")
    searched = request.GET.get("searched", "")

    if not searched and selected in [e.value for e in SelectorEnum]:
        return render(request, "search/search.html")

    if selected == SelectorEnum.EVERYTHING.value:
        obj_split = 8
        news_list = news_filter(searched)
        event_list = event_filter(searched)
        staff_list = staff_filter(searched)
        phd_list = phd_filter(searched)
        project_list = project_filter(searched)
        combined_list = list(chain(news_list, event_list, staff_list, phd_list, project_list))
        combined, page_range = pagination(combined_list, obj_split, page)

        return render(
            request,
            "search/search.html",
            {
                "searched": searched,
                "objects": combined,
                "objects_list": combined_list,
                "page_range": page_range,
                "search_project": project_list,
            },
        )

    elif selected == SelectorEnum.NEWS.value:
        news_list = news_filter(searched)
        news, page_range = pagination(news_list, obj_split, page)
        if len(news_list):
            latest_news = news_list[0]
        else:
            latest_news = 0
        return render(
            request,
            "search/search.html",
            {
                "searched": searched,
                "objects": news,
                "objects_list": news_list,
                "page_range": page_range,
                "latest_news": latest_news,
            },
        )

    elif selected == SelectorEnum.PROJECTS.value:
        project_list = project_filter(searched)
        projects, page_range = pagination(project_list, obj_split, page)
        return render(
            request,
            "search/search.html",
            {"searched": searched, "objects": projects, "objects_list": project_list, "page_range": page_range},
        )

    elif selected == SelectorEnum.PHD.value:
        phd_list = phd_filter(searched)
        phds, page_range = pagination(phd_list, obj_split, page)
        return render(
            request,
            "search/search.html",
            {"searched": searched, "objects": phds, "objects_list": phd_list, "page_range": page_range},
        )

    elif selected == SelectorEnum.EVENTS.value:
        event_list = event_filter(searched)
        events, page_range = pagination(event_list, obj_split, page)
        if len(event_list):
            latest_event = event_list[0]
        else:
            latest_event = 0
        return render(
            request,
            "search/search.html",
            {
                "searched": searched,
                "objects": events,
                "objects_list": event_list,
                "page_range": page_range,
                "latest_event": latest_event,
            },
        )

    elif selected == SelectorEnum.STAFF.value:
        staff_list = staff_filter(searched)
        staffs, page_range = pagination(staff_list, obj_split, page)
        return render(
            request,
            "search/search.html",
            {"searched": searched, "objects": staffs, "objects_list": staff_list, "page_range": page_range},
        )

    return HttpResponseBadRequest()
