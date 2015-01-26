from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

import campaigns.models

class EventAdmin(OrderedModelAdmin):
    list_display = ('content', 'move_up_down_links',)

class NoteAdmin(OrderedModelAdmin):
    list_display = ('title', 'move_up_down_links')

admin.site.register(campaigns.models.Campaign)
admin.site.register(campaigns.models.Session)
admin.site.register(campaigns.models.Event, EventAdmin)
admin.site.register(campaigns.models.Note, NoteAdmin)

