from django.shortcuts import render
from .models import Topic, Newspaper, Redactor


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
