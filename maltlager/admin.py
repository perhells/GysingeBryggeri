from django.contrib import admin

from maltlager.models import malt, hops, maltchange, hopschange

admin.site.register(malt)
admin.site.register(hops)
admin.site.register(maltchange)
admin.site.register(hopschange)
