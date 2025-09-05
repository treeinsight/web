from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.core.exceptions import ValidationError
import datetime
from .crypto import MyCrypto
from .models import SajuEvent, TICalendar
from .models import GOE64_CODE
from .forms import SajuEventForm


class SajuEventCreateView(LoginRequiredMixin, CreateView):

    model = SajuEvent

    template_name = 'sajuevent_create.html'
    login_url = '/account/login'
    form_class = SajuEventForm


    # form_valid 메소드 실행이 끝나면, 데이터가 저장됨
    def form_valid(self, form):

        # template에서는 userid를 직접 입력받지 않으므로, 이곳에서 넣어줘야 함
        form.instance.userid = self.request.user
        try:
            # template에서 구한 효의 조합으로 괘를 구하여 동효와 함께 db에 저장함(참고로 hyo1, hyo2, ...는 template의 hidden요소)
            # form.cleaned_data에는 input요소(hidden 포함)가 없으므로, request.POST에서 직접 가져오는 것임
            goe = self.request.POST["hyo1"] + self.request.POST["hyo2"] + self.request.POST["hyo3"] + self.request.POST["hyo4"] + self.request.POST["hyo5"] + self.request.POST["hyo6"]
            goe_num = GOE64_CODE[goe]
            donghyo = self.request.POST["hyo7"]

            form.instance.goe = goe_num    #GOE64_CODE에서 반환되는 값은 int이므로, 그대로 저장할 것
            form.instance.donghyo = donghyo

        except:
            pass

        try:
            eventyear = form.cleaned_data["eventyear"]
            eventmonth = form.cleaned_data["eventmonth"]
            eventday = form.cleaned_data["eventday"]
            event_datekey = eventyear + eventmonth + eventday

            # 날짜 형식이 맞는 지는 forms.py에서 검토했으므로, 현재 대상 이벤트에 해당하는 TICalendar 객체를 불러온다.
            # (Local DB에 machine_ticalendar가 저장되어 있지 않으면 에러가 발생되어 pass되지만 괜찮음 )
            event_tical = TICalendar.objects.filter(solardate=event_datekey).get()

            # db에 저장할 것
            form.instance.datekey = event_tical
        except:
            pass

        # ===========================================================================================================
        # sajuevent속성 중 title, eventmemo, luckmemo, note는 암호화 작업을 해야함
        # (form.cleaned_data에 입력이 검증된 title 등이 담겨 있으므로 request.POST가 아닌 form.cleaned_data에서 가져올 것)
        try:
            crypto = MyCrypto()
            form.instance.title = crypto.encrypt(form.cleaned_data["title"])
            form.instance.eventmemo = crypto.encrypt(form.cleaned_data["eventmemo"])
            form.instance.luckmemo = crypto.encrypt(form.cleaned_data["luckmemo"])
            form.instance.note = crypto.encrypt(form.cleaned_data["note"])
        except:
            pass
        # ===========================================================================================================

        return super().form_valid(form)


    def get_success_url(self):
        return reverse('machine:detail', kwargs={'pk': self.object.pk})


class SajuEventUpdateView(LoginRequiredMixin, UpdateView):
    '''
    주의사항 : UpdateView에서는 논리상 데이터를 불러올 때 복호화, 수정하여 저장할 때 암호화가 이루어져야 함
    '''

    model = SajuEvent

    template_name = 'sajuevent_update.html'
    login_url = '/account/login'
    form_class = SajuEventForm


    def get_object(self, queryset=None):
        '''
        주의사항 :
        반드시 DetailView에서 context를 업데이트하기 위해서는 get_object()를 오버라이드해야함.
        이유는 복호화 과정 때문에 Data가 로딩되는 과정에 개입해야 하는데,
        get_queryset(), get_context_data()는 나중에 get_object()에서 최초의 context를 읽는 절차 때문에,
        애써서 변경한 context가 template에 적용않기 때문임. (디버그를 걸어놓고, 하나씩 django 코드 속으로 Stepin해가면 알 수 있음)
        '''


        # 현재 대상 이벤트를 필터링하여 불러온다.
        event_queryset = SajuEvent.objects.filter(pk=self.kwargs["pk"])
        event = event_queryset.get()

        # ======================================================================
        # event속성 중 title, eventmemo, luckmemo, note는 복호화 작업을 해야함
        try:
            crypto = MyCrypto()
            event.title = crypto.decrypt(event.title)
            event.eventmemo = crypto.decrypt(event.eventmemo)
            event.luckmemo = crypto.decrypt(event.luckmemo)
            event.note = crypto.decrypt(event.note)
        except:
            pass
        # ======================================================================

        return event


    # form_valid 메소드 실행이 끝나면, 데이터가 저장됨
    def form_valid(self, form):

        # update단계에서는 이미 userid가 입력되어 있으므로 다시 넣어줄 필요가 없음

        # ===========================================================================================================
        # form에 복호화되어 올라온 sajuevent속성 중 title, eventmemo, luckmemo, note는 다시 암호화 작업을 해야함
        # (form.cleaned_data에 입력이 검증된 title 등이 담겨 있으므로 request.POST가 아닌 form.cleaned_data에서 가져올 것)
        try:
            crypto = MyCrypto()
            form.instance.title = crypto.encrypt(form.cleaned_data["title"])
            form.instance.eventmemo = crypto.encrypt(form.cleaned_data["eventmemo"])
            form.instance.luckmemo = crypto.encrypt(form.cleaned_data["luckmemo"])
            form.instance.note = crypto.encrypt(form.cleaned_data["note"])
        except:
            pass
        # ===========================================================================================================

        return super().form_valid(form)


    # 작업이 끝나면, detail 페이지로 이동
    def get_success_url(self):
        return reverse('machine:detail', kwargs={'pk': self.object.pk})


class SajuEventListView(LoginRequiredMixin, ListView):

    model = SajuEvent

    template_name = 'sajuevent_list.html'
    login_url = '/account/login'
    success_url = '/'
    paginate_by = 100  # 한 페이지에 표시할 게시물 개수


    def get_queryset(self):

        # 현재 사용자의 SajuEventList를 필터링하여 불러온다.
        event_list = SajuEvent.objects.filter(userid=self.request.user).order_by('-eventyear','-eventmonth','-eventday','-eventtime')

        try:
            crypto = MyCrypto()

            for i in range(len(event_list)):
                # ===========================================================================
                # sajuevent 속성중 title은 복호화 작업을 해야함(이벤트목록에서 필요한 정보는 title 뿐임)
                # (복호화 작업시 예외처리를 했기 때문에, 암호화되지 않은 문자열도 DB에서 로딩할 수 있음)

                try:
                    event_list[i].title = crypto.decrypt(event_list[i].title)
                except:
                    # 예외발생 목록
                    # print(str(i) + '' + event_list[i].title)
                    pass
                # ===========================================================================
        except:
            pass

        return event_list


    def get_paginate_by(self, queryset):
        return self.request.GET.get("paginate_by", self.paginate_by)


    # def get_context_data(self, **kwargs):
    #
    #     # Call the base implementation first to get the context
    #     context = super(SajuEventListView, self).get_context_data(**kwargs)
    #
    #     # context['my_var'] = 'Hello'
    #
    #     return context


class SajuEventDetailView(LoginRequiredMixin, DetailView):

    model = SajuEvent

    template_name = 'sajuevent_detail.html'
    login_url = '/account/login'
    context_object_name = 'event'


    def get_object(self, queryset=None):
        '''
        주의사항 :
        반드시 DetailView에서 context를 업데이트하기 위해서는 get_object()를 오버라이드해야함.
        이유는 복호화 과정 때문에 Data가 로딩되는 과정에 개입해야 하는데,
        get_queryset(), get_context_data()는 나중에 get_object()에서 최초의 context를 읽는 절차 때문에,
        애써서 변경한 context가 template에 적용않기 때문임. (디버그를 걸어놓고, 하나씩 django 코드 속으로 Stepin해가면 알 수 있음)
        '''


        # 현재 대상 이벤트를 필터링하여 불러온다.
        event_queryset = SajuEvent.objects.filter(pk=self.kwargs["pk"])
        event = event_queryset.get()

        # ======================================================================
        # event속성 중 title, eventmemo, luckmemo, note는 복호화 작업을 해야함
        try:
            crypto = MyCrypto()
            event.title = crypto.decrypt(event.title)
            event.eventmemo = crypto.decrypt(event.eventmemo)
            event.luckmemo = crypto.decrypt(event.luckmemo)
            event.note = crypto.decrypt(event.note)
        except:
            pass
        # ======================================================================

        return event


class SajuEventDeleteView(LoginRequiredMixin, DeleteView):

    model = SajuEvent

    template_name = 'sajuevent_delete.html'
    login_url = '/account/login'
    success_url = reverse_lazy('machine:list')

