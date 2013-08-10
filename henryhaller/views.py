from django.template import Context, RequestContext, loader
from django.http import HttpResponse

import henryhaller.models

HOME_TEMPLATE="home.html"
PERMALINK_TEMPLATE="permalink.html"

TEXT_DIR="/home/ubuntu/sites/django_dir/henryhaller/texts/"
SELF_DESCRIPTION_HTML = TEXT_DIR + "self_description.html"
BLUSERVE_HTML = TEXT_DIR + "bluserve.html"
PORTFOLIO_HTML = TEXT_DIR + "portfolio.html"

def under_construction(request):
    return HttpResponse("Site Under Construction. Check Back soon")

def generate_blog():
    posts = henryhaller.models.BlogPost.objects.order_by("-pk")[:5]
    blog_html = ""
    for post in posts:
        post_html = '<h4 style="post_title"><span class="post_title_span">%s</span> &nbsp; <span class="post_date">%s</span></h4><div style="blog_post">%s</div>' % (post.title, post.pretty_age(), post.text)
        blog_html += post_html
    return blog_html

def permalink(request, short_form_url):
    cd = dict()
    post = henryhaller.models.BlogPost.objects.get(url_title=short_form_url)
    cd["post"] = post
    cd["pretty_age"] = post.pretty_age()
    template = loader.get_template(PERMALINK_TEMPLATE)
    context = RequestContext(request, cd)
    return HttpResponse(template.render(context))
	
    #except: return HttpResponse("that blogpost was not found: " +short_form_url)

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

    #find which was requested, blog, self_description, bluserve
    cd["self_description_display"] = cd["blog_display"] = cd["bluserve_display"] = cd["portfolio_display"] = "none;"
    if request.path in ["/blog", "/blog/"]: cd["blog_display"] = "block;" 
    elif request.path in ["/bluserve", "/bluserve/"]: cd["bluserve_display"] = "block;"
    elif request.path in ["/portfolio", "/portfolio/"]: cd["bluserve_display"] = "block;"
    else: cd["self_description_display"] = "block;"

    template = loader.get_template(HOME_TEMPLATE)
    context = RequestContext(request, cd)
    return HttpResponse(template.render(context))
