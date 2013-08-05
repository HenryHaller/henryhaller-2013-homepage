from django.template import Context, RequestContext, loader
from django.http import HttpResponse


HOME_TEMPLATE="home.html"

TEXT_DIR="/home/ubuntu/sites/django_dir/henryhaller/texts/"
SELF_DESCRIPTION_HTML = TEXT_DIR + "self_description.html"
BLUSERVE_HTML = TEXT_DIR + "bluserve.html"
PORTFOLIO_HTML = TEXT_DIR + "portfolio.html"

def generate_blog():
    return "<p>Blog coming soon.</p>"


def home(request):
    #read in some important datas
    self_description = open(SELF_DESCRIPTION_HTML, 'r').read()
    bluserve = open(BLUSERVE_HTML, 'r').read()
    portfolio = open(PORTFOLIO_HTML, 'r').read()

    cd = dict()

    cd["self_description"] = self_description
    cd["blog"] = generate_blog()
    cd["bluserve"] = bluserve
    cd["portfolio"] = portfolio

    cd["self_description_display"] = cd["blog_display"] = cd["bluserve_display"] = cd["portfolio_display"] = "none;"
    if request.path in ["/blog", "/blog/"]: cd["blog_display"] = "block;" 
    elif request.path in ["/bluserve", "/bluserve/"]: cd["bluserve_display"] = "block;"
    elif request.path in ["/portfolio", "/portfolio/"]: cd["bluserve_display"] = "block;"
    else: cd["self_description_display"] = "block;"

    ua_list = request.META["HTTP_USER_AGENT"]
    cd["size_large"] = cd["size_small"] = False
    if "iPhone" in ua_list or "Phone" in ua_list: cd["size_small"] = True
    else: cd["size_large"] = True

    template = loader.get_template(HOME_TEMPLATE)
    context = RequestContext(request, cd)
    return HttpResponse(template.render(context))
