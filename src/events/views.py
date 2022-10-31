from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils import timezone

from .models import EventModel


def event_list(request):
    object_split = 5
    current_event_list = EventModel.objects.filter(
        Q(event_date__gte=timezone.now()) | Q(event_date_end__gte=timezone.now())
    ).order_by("event_date")
    paginator = Paginator(current_event_list, object_split)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    page_range = paginator.page_range
    past_events = latest_event = None
    if page_obj.number == 1:
        # Only display max 5 past events on the first page
        past_events = EventModel.objects.filter(Q(event_date_end__lt=timezone.now())).order_by("-event_date")[:5]

        # only display featured event on the first page
        if len(current_event_list):
            latest_event = current_event_list[0]
        else:
            latest_event = 0
    return render(
        request,
        "event/event_list.html",
        {"objects": page_obj, "page_range": page_range, "latest_event": latest_event, "past_events": past_events},
    )


def event_full(request, slug):
    event = EventModel.objects.filter(slug=slug).first()
    if not event:
        return HttpResponseNotFound()
    return render(request, "event/event_full.html", {"event": event})


def list_by_tag(request, tag_slug):
    object_split = 5
    event_list = EventModel.objects.filter(tags__slug=tag_slug).order_by("event_date")
    if len(event_list) == 0:
        return HttpResponseNotFound()
    paginator = Paginator(event_list, object_split)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)
    page_range = paginator.page_range
    return render(
        request,
        "event/event_list.html",
        {"objects": page_obj, "page_range": page_range, "latest_event": None, "past_events": None, "tag": tag_slug},
    )
