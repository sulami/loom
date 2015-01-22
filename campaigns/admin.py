from django.contrib import admin

import campaigns.models

admin.site.register(campaigns.models.Campaign)
admin.site.register(campaigns.models.Session)
admin.site.register(campaigns.models.Thread)
admin.site.register(campaigns.models.Event)
admin.site.register(campaigns.models.Note)

