from django.conf.urls import url

from . import views


urlpatterns = [
    url(
        regex=r"^$",
        view=views.EventListView.as_view(),
        name="list"
    ),
    url(
        regex=r"^add/$",
        view=views.EventCreateView.as_view(),
        name="add"
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/$",
        view=views.EventDetailView.as_view(),
        name="detail"
    ),
    url(
        regex=r"^(?P<slug>[-\w]+)/update/$",
        view=views.EventUpdateView.as_view(),
        name="update"
    )
]