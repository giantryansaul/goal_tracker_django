from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r"^$",
        view=views.GoalListView.as_view(),
        name="list"
    ),
    url(
        regex=r"^add/$",
        view=views.GoalCreateView.as_view(),
        name="add"
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/$",
        view=views.GoalDetailView.as_view(),
        name="detail"
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/update/$",
        view=views.GoalUpdateView.as_view(),
        name="update"
    )
]