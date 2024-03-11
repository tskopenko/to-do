from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5
    ordering = ['is_done', '-datetime']


class TaskCreateView(generic.CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('core:task-list')


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('core:task-list')


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('core:task-list')


class TagListView(generic.ListView):
    model = Tag
    context_object_name = 'tag_list'
    template_name = 'core/tag_list.html'
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy("core:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = '__all__'
    success_url = reverse_lazy("core:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("core:tag-list")


def mark_is_complete(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.is_done = True
    task.save()
    return HttpResponseRedirect(
        request.META.get("HTTP_REFERER",
                         reverse_lazy(viewname="core:index"))
    )


def mark_not_complete(request: HttpRequest, pk: int) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.is_done = False
    task.save()
    return HttpResponseRedirect(
        request.META.get("HTTP_REFERER",
                         reverse_lazy(viewname="core:index"))
    )
