from django.contrib import admin
from .models import Project, Partner
from modeltranslation.admin import TabbedTranslationAdmin


class ProjectAdmin(TabbedTranslationAdmin):
    pass


class PartnerAdmin(TabbedTranslationAdmin):
    pass


admin.site.register(Project, ProjectAdmin)
admin.site.register(Partner, PartnerAdmin)
