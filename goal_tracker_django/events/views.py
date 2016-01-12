from django.views.generic import ListView, DetailView, UpdateView, CreateView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Event


class EventListView(ListView):

    paginate_by = 20

    queryset = Event


class EventDetailView(DetailView):

    model = Event


class EventUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    model = Event

    # permission_required = 'events.change_event'
    # raise_exception = True
    # TODO: Add permissions.


class EventCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    model = Event

    # permission_required = 'events.add_event'
    # raise_exception = True
    # TODO: Add permissions.