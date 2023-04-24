from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import Topic, Newspaper, Redactor
from .forms import RedactorCreationForm, NewspaperCreationUpdateForm


def index(requests):
    num_topics = Topic.objects.count()
    num_newspapers = Newspaper.objects.count()
    num_redactor = Redactor.objects.count()

    num_visits = requests.session.get("num_visits", 0)
    requests.session["num_visits"] = num_visits + 1

    context = {
        "num_topics": num_topics,
        "num_newspapers": num_newspapers,
        "num_redactor": num_redactor,
        "num_visits": num_visits
    }
    return render(requests, "newspaper/index.html", context=context)


class TopicListView(generic.ListView):
    model = Topic
    paginate_by = 5


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDetailView(generic.DetailView):
    model = Topic
    fields = "__all__"


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("newspaper:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("newspaper:topic-list")


class NewspaperListView(generic.ListView):
    model = Newspaper
    paginate_by = 5


class NewspaperDetailView(generic.DetailView):
    model = Newspaper
    fields = "__all__"


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    form_class = NewspaperCreationUpdateForm
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    form_class = NewspaperCreationUpdateForm
    success_url = reverse_lazy("newspaper:newspaper-list")


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("newspaper:newspaper-list")


class RedactorListView(generic.ListView):
    model = Redactor
    paginate_by = 5


class RedactorDetailView(generic.DetailView):
    model = Redactor
    fields = "__all__"


class RedactorCreateView(generic.CreateView):
    model = Redactor
    form_class = RedactorCreationForm
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("newspaper:redactor-list")


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("newspaper:redactor-list")
