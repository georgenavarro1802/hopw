from django.contrib import admin

from app.models import Aboutus, Services, Whyus, Projects, Team, Newsletter, Clients, Contacts, Company, Construction


class AboutusAdmin(admin.ModelAdmin):
    list_display = ('words', 'icon1_title', 'icon2_title', 'icon3_title', 'icon4_title')
    search_fields = ('words', 'icon1_title', 'icon2_title', 'icon3_title', 'icon4_title')

admin.site.register(Aboutus, AboutusAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('header1', 'header2', 'icon1_title', 'icon2_title', 'icon3_title')
    search_fields = ('icon1_title', 'icon2_title', 'icon3_title')

admin.site.register(Services, ServicesAdmin)


class WhyusAdmin(admin.ModelAdmin):
    list_display = ('header1', 'header2', 'icon1_title', 'icon2_title', 'icon3_title', 'icon4_title')
    search_fields = ('icon1_title', 'icon2_title', 'icon3_title', 'icon4_title')

admin.site.register(Whyus, WhyusAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('header1', 'header2', 'icon1_title', 'icon2_title', 'icon3_title', 'icon4_title',
                    'icon5_title', 'icon6_title', 'icon7_title', 'icon8_title')
    search_fields = ('icon1_title', 'icon2_title', 'icon3_title', 'icon4_title')

admin.site.register(Projects, ProjectsAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('header1', 'header2', 'icon1_name', 'icon2_name', 'icon3_name', 'icon4_name')
    search_fields = ('icon1_name', 'icon2_name', 'icon3_name', 'icon4_name')

admin.site.register(Team, TeamAdmin)


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created')
    search_fields = ('email', )
    ordering = ('created', )

admin.site.register(Newsletter, NewsletterAdmin)


class ClientsAdmin(admin.ModelAdmin):
    list_display = ('header1', 'header2')
    search_fields = ('header1', 'header2')

admin.site.register(Clients, ClientsAdmin)


class ContactsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'contact_type', 'email', 'message', 'created')
    search_fields = ('first_name', 'last_name')
    ordering = ('created', )
    list_filter = ('contact_type', )

admin.site.register(Contacts, ContactsAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone')
    search_fields = ('name', 'address')

admin.site.register(Company, CompanyAdmin)


class ConstructionAdmin(admin.ModelAdmin):
    list_display = ('header1', 'header2', 'subservices')
    search_fields = ('header1', 'header2')

admin.site.register(Construction, ConstructionAdmin)