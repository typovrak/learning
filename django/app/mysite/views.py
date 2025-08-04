from django.http import HttpResponse
from django.template import loader


# @require_http_methods(["GET"])
def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())
