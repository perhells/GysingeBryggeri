from django.contrib import admin

from maltlager.models import Malt, Hops, MaltChange, HopsChange

admin.site.register(Malt)
admin.site.register(Hops)
admin.site.register(MaltChange)
admin.site.register(HopsChange)
