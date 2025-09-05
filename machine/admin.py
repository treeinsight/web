# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import ActorCategory,ActCategory
from .models import Actor,Act,Source,Theory
from .models import Saju,SajuParsing,SajuNote,TICalendar,HistoryEvent,SajuEvent
from .models import Iching,IchingNote,IchingCase
from .models import WebMonitor,WebMonitorLog
from .models import Message
from .models import Registry


class HistoryEventAdmin(admin.ModelAdmin):
    #Admin에서 ListBox형태가 아닌, TextBox로 입력할 수 있게 한다.
    raw_id_fields = ("datekey",)

class SajuEventAdmin(admin.ModelAdmin):
    #Admin에서 ListBox형태가 아닌, TextBox로 입력할 수 있게 한다.
    raw_id_fields = ("datekey",)

class IchingCaseAdmin(admin.ModelAdmin):
    #Admin에서 ListBox형태가 아닌, TextBox로 입력할 수 있게 한다.
    raw_id_fields = ("datekey",)

admin.site.register(ActorCategory)
admin.site.register(ActCategory)
admin.site.register(Actor)
admin.site.register(Act)
admin.site.register(Source)
admin.site.register(Theory)
admin.site.register(Saju)
admin.site.register(SajuParsing)
admin.site.register(SajuNote)
admin.site.register(TICalendar)
admin.site.register(HistoryEvent, HistoryEventAdmin)
admin.site.register(SajuEvent, SajuEventAdmin)
admin.site.register(Iching)
admin.site.register(IchingNote)
admin.site.register(IchingCase, IchingCaseAdmin)
admin.site.register(WebMonitor)
admin.site.register(WebMonitorLog)
admin.site.register(Message)
admin.site.register(Registry)
