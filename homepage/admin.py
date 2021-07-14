from django.contrib import admin

# Register your models here.


from.models import MarkettingEmail,EmailSubscribers
admin.site.site_header= 'Sky-Swift Admin'






class EmailSubscriberss(admin.ModelAdmin):
    list_display = ('email',)
admin.site.register(EmailSubscribers,EmailSubscriberss)


class MarkettingEmails(admin.ModelAdmin):

    list_display = ('email',)
admin.site.register(MarkettingEmail,MarkettingEmails)





