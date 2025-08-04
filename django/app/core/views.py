from django.http import HttpResponse
from django.template import loader


# @require_http_methods(["GET"])
def index(request):
    template = loader.get_template("index.html")
    context = {
        "blog_entries": [
            {
                "title": "test1",
                "body": "body1",
            },
            {
                "title": "test2",
                "body": "body2",
            },
        ]
    }

    return HttpResponse(template.render(context, request))
