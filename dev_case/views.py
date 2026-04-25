from django.db.models import Q
from django.shortcuts import render

from blog.models import BlogPost
from config.models import MainConfig, SocialAccountsConfig
from pages.models import AboutSiteConfig, IndexSiteConfig
from portfolio.models import Certification, Experience, Project, Publication

from .settings import ROBOTS_DISALLOW
from .sitemaps import get_sitemap_absolute_url


def home(request):
    index_config = IndexSiteConfig.get_solo()
    social_accounts = SocialAccountsConfig.get_solo()
    main_config = MainConfig.get_solo()
    posts = BlogPost.objects.prefetch_related("category").filter(status=1)[:3]
    projects = Project.objects.filter(status=1)
    context = {
        "index_config": index_config,
        "social_accounts": social_accounts,
        "main_config": main_config,
        "posts": posts,
        "projects": projects,
    }
    return render(request, "index.html", context=context)


def about(request):
    about_config = AboutSiteConfig.get_solo()
    social_accounts = SocialAccountsConfig.get_solo()
    context = {
        "about_config": about_config,
        "social_accounts": social_accounts,
    }
    return render(request, "about.html", context=context)


def certifications(request):
    certifications = Certification.objects.all().order_by("-date")
    social_accounts = SocialAccountsConfig.get_solo()
    context = {
        "certifications": certifications,
        "social_accounts": social_accounts,
    }
    return render(request, "certifications.html", context=context)


def publications(request):
    publications = Publication.objects.all().order_by("-date")
    social_accounts = SocialAccountsConfig.get_solo()
    context = {
        "publications": publications,
        "social_accounts": social_accounts,
    }
    return render(request, "publications.html", context=context)


def experience(request):
    experiences = Experience.objects.all().order_by("-start_date")
    social_accounts = SocialAccountsConfig.get_solo()
    context = {
        "experiences": experiences,
        "social_accounts": social_accounts,
    }
    return render(request, "experience.html", context=context)


def search(request):
    posts = {}
    if request.method == "GET":
        query = request.GET.get("q")
        if query:
            posts = BlogPost.objects.filter(
                Q(title__icontains=query) | Q(category__name__icontains=query)
            )
    context = {
        "posts": posts,
    }
    return render(request, "search.html", context=context)


def robots_txt(request):
    context = {
        "sitemap": get_sitemap_absolute_url(request),
        "disallow": ROBOTS_DISALLOW,
    }
    return render(request, "robots.txt", context=context, content_type="text/plain")
