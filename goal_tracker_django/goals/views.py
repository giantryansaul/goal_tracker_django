from django.views.generic import ListView, DetailView, UpdateView, CreateView

from braces.views import LoginRequiredMixin, PermissionRequiredMixin

from .models import Goal


class GoalListView(ListView):

    paginate_by = 20

    queryset = Goal


class GoalDetailView(DetailView):

    model = Goal


class GoalUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):

    model = Goal

    permission_required = 'goals.change_goal'
    raise_exception = True


class GoalCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):

    model = Goal

    permission_required = 'goals.add_goal'
    raise_exception = True