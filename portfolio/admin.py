from django.contrib import admin

from .models import Certification, Experience, Project, Publication, TechStack, Tool


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created")
    list_filter = ("status", "created")
    search_fields = ("title", "author")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("status",)


@admin.register(TechStack)
class TechStackAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "issuer", "date")
    list_filter = ("issuer", "date")
    search_fields = ("name", "issuer")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "end_date", "is_current")
    list_filter = ("company", "start_date", "is_current")
    search_fields = ("position", "company")


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ("title", "journal", "date")
    list_filter = ("journal", "date")
    search_fields = ("title", "journal", "doi")
