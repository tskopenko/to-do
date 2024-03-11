from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    paginate_by = 5


class TaskDetailView(generic.DetailView):
    model = Task


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
