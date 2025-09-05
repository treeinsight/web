# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
import datetime
from .models import Saju,SajuEvent,IchingCase


class SajuForm(ModelForm):

    class Meta:
        model = Saju
        fields = ('name', 'gender','birthdate','birthtime',)


class SajuEventForm(ModelForm):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.attrs = {'novalidate': ''}
        self.helper.form_tag = False                # this will make sure no additional <form> tag (이 부분을 넣지 않으면 submit 버튼이 작동하지 않음)
        self.helper.disable_csrf = True             # this will make sure no additional csrf (이 부분을 넣지 않으면 submit 버튼이 작동하지 않음)

        self.helper.layout = Layout(
            'title',
            Row(
                Column('eventyear', css_class='form-group col-md-3 mb-0'),
                Column('eventmonth', css_class='form-group col-md-3 mb-0'),
                Column('eventday', css_class='form-group col-md-3 mb-0'),
                Column('eventtime', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('weather', css_class='form-group col-md-4 mb-0'),
                Column('eventlocation', css_class='form-group col-md-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('actorid', css_class='form-group col-md-3 mb-0'),
                Column('actid', css_class='form-group col-md-6 mb-0'),
                Column('category', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'eventmemo',
            Row(
                Column('wealthindex', css_class='form-group col-md-1 mb-0'),
                Column('healthindex', css_class='form-group col-md-1 mb-0'),
                Column('jobindex', css_class='form-group col-md-1 mb-0'),
                Column('relationindex', css_class='form-group col-md-1 mb-0'),
                Column('studyindex', css_class='form-group col-md-1 mb-0'),
                Column('honorindex', css_class='form-group col-md-1 mb-0'),
                Column('moveindex', css_class='form-group col-md-1 mb-0'),
                Column('outcomeindex', css_class='form-group col-md-1 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('goe_expected', css_class='form-group col-md-10 mb-0'),
                Column('donghyo_expected', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'luckmemo',
            'note',
            'url1',
        )


    def clean_eventyear(self):
        '''
        eventyear 필드값 검증
        '''

        data = self.cleaned_data['eventyear']

        # 텍스트 숫자인지 확인
        try:
            check_value = int(data)
        except:
            raise ValidationError("숫자로 입력해야 합니다. (Ex. 2021)")

        # 자릿수 확인
        if not len(data) == 4:
            raise ValidationError("4자리의 숫자로 입력해야 합니다. (Ex. 2021)")

        return data


    def clean_eventday(self):
        '''
        eventday 필드값 체크 단계에서 전체 날짜의 형식적 타당성 여부 검토
        '''

        eventyear = self.cleaned_data["eventyear"]
        eventmonth = self.cleaned_data["eventmonth"]
        data = self.cleaned_data["eventday"]

        # 날짜 형식이 맞는 지 확인
        try:
            temp = datetime.datetime(year=int(eventyear), month=int(eventmonth), day=int(data))
        except:
            raise ValidationError("연,월,일의 조합이 정확한 날짜가 되어야 합니다! (Ex. 20210720)")

        return data


    class Meta:

        model = SajuEvent

        # 'userid'는 view 로직에서, 'goe', 'donghyo'는 template에서 hidden 요소로 자동 전달
        # 나머지 주석처리된 필드는 일단 현재 로직에서는 입력하지 않음
        # datekey는 레코드수가 많으므로 양식에 로딩하기에 매우 시간이 걸림
        fields = ('title',
                  'datekey','eventyear', 'eventmonth', 'eventday', 'eventtime',
                  # 'yeargan', 'yearji', 'monthgan', 'monthji', 'daygan', 'dayji', 'timegan', 'timeji',
                  'weather', 'eventlocation',
                  # 'daewoongan', 'daewoonji', 'sewoongan', 'sewoonji',
                  'actorid', 'actid', 'category', 'eventmemo',
                  'wealthindex', 'healthindex', 'jobindex', 'relationindex', 'studyindex', 'honorindex', 'moveindex', 'outcomeindex',
                  'goe_expected', 'donghyo_expected',
                  'luckmemo', 'note', 'url1',
                  # 'tipedia', 'url2', 'url3',
                  )


class IchingCaseForm(ModelForm):

    class Meta:
        model = IchingCase
        fields = ('question','ichingyear','ichingmonth','ichingday','ichingtime','weather','ichinglocation',)
        fields += ('category','goe','donghyo1','donghyo2','donghyo3','donghyo4','donghyo5','donghyo6',)
        fields += ('futureluckindex','futureluckmemo','resultluckindex','resultluckmemo','matchpercent','expiredtime',)

