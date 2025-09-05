# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models import JSONField
from .crypto import MyCrypto


CHECKSTATUS3 = (
    (1, '확인'),
    (2, '미확인'),
    (3, '에러'),
    )

GRADE5 = (
    (-2, '매우 흉함'),
    (-1, '흉함'),
    (0, '보통'),
    (1,'길함'),
    (2,'매우 길함'),
    )

GENDER = (
    (1, '남자'),
    (2, '여자'),
    (3, '기타'),
    )

GAN = (
    ('a', '甲'),('b', '乙'),('c', '丙'),('d', '丁'),('e', '戊'),
    ('f', '己'),('g', '庚'),('h', '辛'),('i', '壬'),('j', '癸'),
    )

JI = (
    ('o', '子'),('p', '丑'),('q', '寅'),('r', '卯'),('s', '辰'),('t', '巳'),
    ('u', '午'),('v', '未'),('w', '申'),('x', '酉'),('y', '戌'),('z', '亥'),
    )

LEAP3 = (
    (0, '평달'),
    (1, '윤달평달'),
    (2, '윤달'),
    )

#초효부터 상효방향으로 음은 2, 양은 3으로 표시
GOE64_CODE = {
'333333':1,'222222':2, '322232':3,'232223':4,'333232':5,'232333':6,'232222':7,'222232':8,'333233':9,'332333':10,
'333222':11,'222333':12,'323333':13,'333323':14,'223222':15,'222322':16,'322332':17,'233223':18,'332222':19,'222233':20,
'322323':21,'323223':22,'222223':23,'322222':24,'322333':25,'333223':26,'322223':27,'233332':28,'232232':29,'323323':30,
'223332':31,'233322':32,'223333':33,'333322':34,'222323':35,'323222':36,'323233':37,'332323':38,'223232':39,'232322':40,
'332223':41,'322233':42,'333332':43,'233333':44,'222332':45,'233222':46,'232332':47,'233232':48,'323332':49,'233323':50,
'322322':51,'223223':52,'223233':53,'332322':54,'323322':55,'223323':56,'233233':57,'332332':58,'232233':59,'332232':60,
'332233':61,'223322':62,'323232':63,'232323':64,
}

GOE64 = (
    (1, '01. 중천건'),(2, '02. 중지곤'),(3, '03. 수뢰둔'),(4, '04. 산수몽'),(5, '05. 수천수'),(6, '06. 천수송'),(7, '07. 지수사'),(8, '08. 수지비'),(9, '09. 풍천소축'),(10, '10. 천택리'),
    (11, '11. 지천태'),(12, '12. 천지비'),(13, '13. 천화동인'),(14, '14. 화천대유'),(15, '15. 지산겸'),(16, '16. 뇌지예'),(17, '17. 택뢰수'),(18, '18. 산풍고'),(19, '19. 지택림'),(20, '20. 풍지관'),
    (21, '21. 화뢰서합'),(22, '22. 산화비'),(23, '23. 산지박'),(24, '24. 지뢰복'),(25, '25. 천뢰무망'),(26, '26. 산천대축'),(27, '27. 산뢰이'),(28, '28. 택풍대과'),(29, '29. 중수감'),(30, '30. 중화리'),
    (31, '31. 택산함'), (32, '32. 뇌풍항'), (33, '33. 천산돈'), (34, '34. 뇌천대장'), (35, '35. 화지진'), (36, '36. 지화명이'),(37, '37. 풍화가인'), (38, '38. 화택규'), (39, '39. 수산건'), (40, '40. 뇌수해'),
    (41, '41. 산택손'), (42, '42. 풍뢰익'), (43, '43. 택천쾌'), (44, '44. 천풍구'), (45, '45. 택지취'), (46, '46. 지풍승'),(47, '47. 택수곤'), (48, '48. 수풍정'), (49, '49. 택화혁'), (50, '50. 화풍정'),
    (51, '51. 중뢰진'), (52, '52. 중산간'), (53, '53. 풍산점'), (54, '54. 뇌택귀매'), (55, '55. 뇌화풍'), (56, '56. 화산려'),(57, '57. 중풍손'), (58, '58. 중택태'), (59, '59. 풍수환'), (60, '60. 수택절'),
    (61, '61. 풍택중부'), (62, '62. 뇌산소과'), (63, '63. 수화기제'), (64, '64. 화수미제'),
    )

HYO6 = (
    (6, '상효'),
    (5, '5효'),
    (4, '4효'),
    (3, '3효'),
    (2, '2효'),
    (1, '초효'),
    )

ICHINGPART = (
    (0, '기타'),
    (1, '주역'),
    (2, '명리'),
    )

PLUS_MINUS = (
    (2, '음(_ _)'),
    (3, '양(___)'),
    )

WEATHER = (
    (0, '기타'),
    (1, '맑음'),
    (2, '맑았다가 흐려짐'),
    (3, '맑았다가 비옴'),
    (4, '흐림'),
    (5, '비옴'),
    (6, '비오다가 갬'),
    )

MOON30 = (
    (1, '1=그믐'),(2, '2'),(3, '3'),(4, '4'),(5, '5'),(6, '6'),
    (7, '7'),(8, '8'),(9, '9'),(10, '10'),(11, '11'),(12, '12'),
    (13, '13'),(14, '14'),(15, '15=보름'),(16, '16'),(17, '17'),(18, '18'),
    (19, '19'),(20, '20'),(21, '21'),(22, '22'),(23, '23'),(24, '24'),
    (25, '25'),(26, '26'),(27, '27'),(28, '28'),(29, '29'),(30, '30'),
    )

WEEK7 = (
    (1, '일'),
    (2, '월'),
    (3, '화'),
    (4, '수'),
    (5, '목'),
    (6, '금'),
    (7, '토'),
    )

MONTH12 = (
    ('01', '양력1월'),('02', '양력2월'),('03', '양력3월'),('04', '양력4월'),('05', '양력5월'),
    ('06', '양력6월'),('07', '양력7월'),('08', '양력8월'),('09', '양력9월'),('10', '양력10월'),
    ('11', '양력11월'),('12', '양력12월'),
    )

DAY31 = (
    ('01', '1일'),('02', '2일'),('03', '3일'),('04', '4일'),('05', '5일'),('06', '6일'),
    ('07', '7일'),('08', '8일'),('09', '9일'),('10', '10일'),('11', '11일'),('12', '12일'),
    ('13', '13일'),('14', '14일'),('15', '15일'),('16', '16일'),('17', '17일'),('18', '18일'),
    ('19', '19일'),('20', '20일'),('21', '21일'),('22', '22일'),('23', '23일'),('24', '24일'),
    ('25', '25일'),('26', '26일'),('27', '27일'),('28', '28일'),('29', '29일'),('30', '30일'),
    ('31', '31일'),
    )

JEOLGI12 = (
    (1, '입춘'),(2, '경칩'),(3, '청명'),(4, '입하'),(5, '망종'),(6, '소서'),
    (7, '입추'),(8, '백로'),(9, '한로'),(10, '입동'),(11, '대설'),(12, '소한'),
    )

ICHINGSECTION = (
    (0, '기타'),
    (1, '건강점'),
    (2, '재물점'),
    (3, '애정점'),
    (4, '학문점'),
    (5, '직장점'),
    (6, '명예점'),
    )

HISTORYSECTION = (
    (0, '기타'),
    (1, '한국사'),
    (2, '중국사'),
    (3, '일본사'),
    (4, '미국사'),
    (5, '유럽사'),
    (6, '러시아사'),
    )


class ActorCategory(models.Model):
    '''
    ActorCategory
    '''

    name = models.CharField(max_length=40, verbose_name='Actor 범주(*)', help_text='Actor(사건 주체) 범주명칭(ex. 0.기타, 1.인물, 2.재물, 3.사회제도...)')
    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL1', help_text='외부 관련 URL 1', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)

    def __str__(self):
        return self.name


class ActCategory(models.Model):
    '''
    ActCategory
    '''

    name = models.CharField(max_length=40, verbose_name='Act 범주(*)', help_text='Act(주체의 작용) 범주명칭(ex. 0.기타, 1.만남, 2.헤어짐, 3.출생, 4.사망, 5.경제적이득, 6.경제적손실...)')
    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL1', help_text='외부 관련 URL 1', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    '''
    Actor :
    주체(體) 즉, '사건 주체'를 말함
    '''

    name = models.CharField(max_length=40, verbose_name='Actor 명칭(*)', help_text='Actor 명칭(ex. 아버지, 어머니, 형제자매, 스승, 제자, 금전, 부동산, 건물, 금리, 판결...)')
    category = models.ForeignKey(ActorCategory, on_delete=models.SET_NULL, verbose_name='Actor 범주', help_text='Actor 범주', blank=True, null=True)
    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL1', help_text='외부 관련 URL 1', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)

    def __str__(self):
        return self.name


class Act(models.Model):
    '''
    Act :
    작용(用) 즉, '주체의 작용'을 말함
    '''

    action = models.CharField(max_length=80, verbose_name='Act 내용(*)', help_text='Act 내용(ex. 건강이 회복되다, 태어나다, 계약이 성사되다, 시험에 합격하다...)')
    category = models.ForeignKey(ActCategory, on_delete=models.SET_NULL, verbose_name='Act 범주', help_text='Act 범주', blank=True, null=True)
    wealthindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='재물지수(*)', help_text='재물 관련도')
    healthindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='건강지수(*)', help_text='건강 관련도')
    jobindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='직장지수(*)', help_text='직장/관운 관련도')
    relationindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='관계지수(*)', help_text='인간관계 관련도')
    studyindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='학업지수(*)', help_text='학업 관련도')
    honorindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='명예지수(*)', help_text='명예 관련도')
    moveindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='이동지수(*)', help_text='이동(여행/전직/부서이동 등) 관련도')
    outcomeindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='성과지수(*)', help_text='성과(연구/예술작품/자녀교육 등) 관련도')
    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL1', help_text='외부 관련 URL 1', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)

    def __str__(self):
        return self.action


class Source(models.Model):
    '''
    Source
    '''

    author = models.CharField(max_length=40, verbose_name='저자(*)', help_text='저자 성명')
    title = models.CharField(max_length=80, default='제목을 입력할 것', verbose_name='제목(*)', help_text='문헌 제목')
    translator = models.CharField(max_length=40, verbose_name='번역자', help_text='번역자 성명', blank=True, null=True)
    section = models.SmallIntegerField(default=1, choices=ICHINGPART, verbose_name='분야(*)', help_text='주역/명리 구분')
    publisher = models.CharField(max_length=40, verbose_name='출판사', help_text='출판사 또는 발행기관', blank=True, null=True)
    publishyear = models.CharField(max_length=4, verbose_name='출판년도', help_text='출판년도를 4자리 숫자로 입력(YYYY)', blank=True, null=True)
    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL1', help_text='외부 관련 URL 1', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)

    def __str__(self):
        return self.author + '- ' + self.title


class Theory(models.Model):
    '''
    Theory
    '''

    title = models.CharField(max_length=80, verbose_name='이론 제목(*)', help_text='이론 제목(ex. 백호살, 도화살, 춘목경금불가, 소강절본괘오행...)')
    researcher = models.CharField(max_length=40, verbose_name='연구자 성명', help_text='명리 연구자 성명', blank=True, null=True)
    contents = models.TextField(verbose_name='이론 내용', help_text='이론 내용', blank=True, null=True)
    section = models.SmallIntegerField(default=1, choices=ICHINGPART, verbose_name='분야(*)', help_text='분야')

    wealthindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='재물지수(*)', help_text='재물 관련도')
    healthindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='건강지수(*)', help_text='건강 관련도')
    jobindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='직장지수(*)', help_text='직장/관운 관련도')
    relationindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='관계지수(*)', help_text='인간관계 관련도')
    studyindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='학업지수(*)', help_text='학업 관련도')
    honorindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='명예지수(*)', help_text='명예 관련도')
    moveindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='이동지수(*)', help_text='이동(여행/전직/부서이동 등) 관련도')
    outcomeindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='성과지수(*)', help_text='성과(연구/예술작품/자녀교육 등) 관련도')

    sourceid = models.ForeignKey(Source, on_delete=models.SET_NULL, verbose_name='출처', help_text='출처 정보', blank=True, null=True)
    sourcememo = models.TextField(verbose_name='출처메모', help_text='출처 메모', blank=True, null=True)
    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL1', help_text='외부 관련 URL 1', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)

    def __str__(self):
        return self.title


class Saju(models.Model):
    '''
    Saju:
    1. 사용자 또는 관리자가 입력
    2. birthdate가 입력되거나, 사주간지가 직접 입력되어야 함
    '''

    userid = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='User ID', help_text='대상 User ID(Null이면 회원 미가입 사주)', blank=True, null=True)
    name = models.CharField(max_length=40, verbose_name='소유자 성명(*)', help_text='사주 소유자 성명(또는 호칭)')
    gender = models.SmallIntegerField(default=1, choices=GENDER, verbose_name='성별(*)', help_text='남자/여자 구분')
    birthdate = models.CharField(max_length=8, verbose_name='생년월일(양력)', help_text='양력 생년월일 입력(YYYYMMDD) ex. 19771213', blank=True, null=True)
    birthtime = models.CharField(max_length=4, verbose_name='생시', help_text='출생 시각을 24시간제 형태로 입력(hhmm) ex. 0020', blank=True, null=True)
    yeargan = models.CharField(max_length=2, choices=GAN, verbose_name='연간', help_text='연간', blank=True, null=True)
    yearji = models.CharField(max_length=2, choices=JI, verbose_name='연지', help_text='연지', blank=True, null=True)
    monthgan = models.CharField(max_length=2, choices=GAN, verbose_name='월간', help_text='월간', blank=True, null=True)
    monthji = models.CharField(max_length=2, choices=JI, verbose_name='월지', help_text='월지', blank=True, null=True)
    daygan = models.CharField(max_length=2, choices=GAN, verbose_name='일간', help_text='일간', blank=True, null=True)
    dayji = models.CharField(max_length=2, choices=JI, verbose_name='일지', help_text='일지', blank=True, null=True)
    timegan = models.CharField(max_length=2, choices=GAN, verbose_name='시간', help_text='시간', blank=True, null=True)
    timeji = models.CharField(max_length=2, choices=JI, verbose_name='시지', help_text='시지', blank=True, null=True)
    sourceid = models.ForeignKey(Source, on_delete=models.SET_NULL, verbose_name='출처', help_text='출처 정보', blank=True, null=True)
    sourcememo = models.TextField(verbose_name='출처메모', help_text='출처 메모', blank=True, null=True)
    createdtime = models.DateTimeField(auto_now_add=True, verbose_name='사주입력날짜', help_text='사주 정보가 시스템에 최초 입력된 날짜와 시간', blank=True, null=True)
    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL1', help_text='외부 관련 URL 1', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)

    def __str__(self):
        return self.name + '(USERID: ' + str(self.userid) + ')'


class SajuParsing(models.Model):
    '''
    SajuParsing:
    SajuParser모듈이 사용자 입력내용(Saju 모델)을 바탕으로 자동계산 및 DB입력
    '''

    sajuid = models.OneToOneField(Saju, on_delete=models.CASCADE, verbose_name='사주ID(*)', help_text='관련되는 사주의 ID')

    ####################################################################
    #이하 SajuNote 모델과 동일
    gender = models.SmallIntegerField(choices=GENDER, verbose_name='성별', help_text='성별', blank=True, null=True)
    yeargan = models.CharField(max_length=2, choices=GAN, verbose_name='연간', help_text='연간', blank=True, null=True)
    yearji = models.CharField(max_length=2, choices=JI, verbose_name='연지', help_text='연지', blank=True, null=True)
    monthgan = models.CharField(max_length=2, choices=GAN, verbose_name='월간', help_text='월간', blank=True, null=True)
    monthji = models.CharField(max_length=2, choices=JI, verbose_name='월지', help_text='월지', blank=True, null=True)
    daygan = models.CharField(max_length=2, choices=GAN, verbose_name='일간', help_text='일간', blank=True, null=True)
    dayji = models.CharField(max_length=2, choices=JI, verbose_name='일지', help_text='일지', blank=True, null=True)
    timegan = models.CharField(max_length=2, choices=GAN, verbose_name='시간', help_text='시간', blank=True, null=True)
    timeji = models.CharField(max_length=2, choices=JI, verbose_name='시지', help_text='시지', blank=True, null=True)

    #대운세운 요소
    daewoongan = models.CharField(max_length=2, choices=GAN, verbose_name='대운천간', help_text='대운천간', blank=True, null=True)
    daewoonji = models.CharField(max_length=2, choices=JI, verbose_name='대운지지', help_text='대운지지', blank=True, null=True)
    sewoongan = models.CharField(max_length=2, choices=GAN, verbose_name='세운천간', help_text='세운천간', blank=True, null=True)
    sewoonji = models.CharField(max_length=2, choices=JI, verbose_name='세운지지', help_text='세운지지', blank=True, null=True)

    #...
    ####################################################################

    def __str__(self):
        return str(self.sajuid)


class SajuNote(models.Model):
    '''
    SajuNote:
    '''

    title = models.CharField(max_length=80, verbose_name='노트 제목', help_text='노트 제목(ex. 백호살, 도화살, 춘목경금불가, 소강절본괘오행...)', blank=True, null=True) #admin에서 보기쉽게 관리하기 위한 필드
    theory = models.ForeignKey(Theory, on_delete=models.CASCADE, verbose_name='이론(*)', help_text='이론 명칭(ex. 백호살, 도화살, 춘목경금불가, 소강절본괘오행...)')   #하나의 이론을 설명하는 여러 레코드를 묶는 코드

    ####################################################################
    #이하 SajuParsing 모델과 동일
    gender = models.SmallIntegerField(choices=GENDER, verbose_name='성별', help_text='성별', blank=True, null=True)
    yeargan = models.CharField(max_length=2, choices=GAN, verbose_name='연간', help_text='연간', blank=True, null=True)
    yearji = models.CharField(max_length=2, choices=JI, verbose_name='연지', help_text='연지', blank=True, null=True)
    monthgan = models.CharField(max_length=2, choices=GAN, verbose_name='월간', help_text='월간', blank=True, null=True)
    monthji = models.CharField(max_length=2, choices=JI, verbose_name='월지', help_text='월지', blank=True, null=True)
    daygan = models.CharField(max_length=2, choices=GAN, verbose_name='일간', help_text='일간', blank=True, null=True)
    dayji = models.CharField(max_length=2, choices=JI, verbose_name='일지', help_text='일지', blank=True, null=True)
    timegan = models.CharField(max_length=2, choices=GAN, verbose_name='시간', help_text='시간', blank=True, null=True)
    timeji = models.CharField(max_length=2, choices=JI, verbose_name='시지', help_text='시지', blank=True, null=True)

    #대운세운 요소
    daewoongan = models.CharField(max_length=2, choices=GAN, verbose_name='대운천간', help_text='대운천간', blank=True, null=True)
    daewoonji = models.CharField(max_length=2, choices=JI, verbose_name='대운지지', help_text='대운지지', blank=True, null=True)
    sewoongan = models.CharField(max_length=2, choices=GAN, verbose_name='세운천간', help_text='세운천간', blank=True, null=True)
    sewoonji = models.CharField(max_length=2, choices=JI, verbose_name='세운지지', help_text='세운지지', blank=True, null=True)

    #...
    ####################################################################

    def __str__(self):
        return str(self.id) + '- ' + self.title


class TICalendar(models.Model):

    '''TICalendar:
    1. 한국천문연구원 DB 기반(1391-2050)
    2. solardate가 primary키여야 ForeignKey로 조회되는 테이블에서 '양력날짜'로 직접 입력할 수 있음
    '''

    id = models.IntegerField(verbose_name='연번', help_text='연번 입력', blank=True, null=True) #primary키는 아니나, 단순 연번을 보관하기 위해 필드 설정

    solardate = models.CharField(max_length=8, verbose_name='양력 연월일(*)', help_text='양력 연월일(YYYYMMDD) ex. 19771213', primary_key=True)
    dayofweek = models.SmallIntegerField(choices=WEEK7, verbose_name='양력 요일', help_text='양력 요일 선택', blank=True, null=True)
    leapmonth = models.SmallIntegerField(choices=LEAP3, verbose_name='윤달', help_text='윤달 여부(0=평달/1=윤달평달/2=윤달)', blank=True, null=True)
    lunardate = models.CharField(max_length=8, verbose_name='음력 연월일', help_text='음력 연월일(YYYYMMDD) ex. 19771103', blank=True, null=True)
    moonstatus = models.SmallIntegerField(choices=MOON30, verbose_name='달 모양', help_text='달 모양 선택(1~30, 1=그믐/15=보름)', blank=True, null=True)

    ganji = models.CharField(max_length=50, verbose_name='연월일 간지', help_text='연월일 간지 ex. 신미(辛未)년 경인(庚寅)월 기축(己丑)일', blank=True, null=True)
    yeargan = models.CharField(max_length=2, choices=GAN, verbose_name='연간(*)', help_text='연간 선택')
    yearji = models.CharField(max_length=2, choices=JI, verbose_name='연지(*)', help_text='연지 선택')
    monthgan = models.CharField(max_length=2, choices=GAN, verbose_name='월간(*)', help_text='월간 선택')
    monthji = models.CharField(max_length=2, choices=JI, verbose_name='월지(*)', help_text='월지 선택')
    daygan = models.CharField(max_length=2, choices=GAN, verbose_name='일간(*)', help_text='일간 선택')
    dayji = models.CharField(max_length=2, choices=JI, verbose_name='일지(*)', help_text='일지 선택')

    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL1', help_text='외부 관련 URL 1', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)

    def __str__(self):
        return str(self.solardate)


class HistoryEvent(models.Model):
    '''HistoryEvent:
    역사적인 사실
    '''

    title = models.CharField(max_length=80, default='제목을 입력할 것', verbose_name='사건 제목(*)', help_text='사건 제목')

    historysection = models.SmallIntegerField(default=0, choices=HISTORYSECTION, verbose_name='역사 범주(*)', help_text='역사 범주(ex. 한국사,중국사,유럽사...)')

    datekey = models.ForeignKey(TICalendar, on_delete=models.SET_NULL, verbose_name='만세력 연결', help_text='양력 연월일(YYYYMMDD ex. 19771213)을 정확히 아는 경우, 입력하면 만세력에 연결됨', blank=True, null=True)
    eventyear = models.CharField(max_length=4, verbose_name='발생연도', help_text='발생연도만 아는 경우, 4자리 숫자로 입력(YYYY, 만세력에 연결되었으면 입력할 필요없음)', blank=True, null=True)
    eventmonth = models.CharField(max_length=2, choices=MONTH12, verbose_name='발생월', help_text='발생연도/발생월만 아는 경우, 양력 발생월 선택(만세력에 연결되었으면 입력할 필요없음)', blank=True, null=True)
    eventday = models.CharField(max_length=2, choices=DAY31, verbose_name='발생일', help_text='발생연도/발생월/발생일을 아는 경우, 양력 발생일 선택(만세력에 연결되었으면 입력할 필요없음)', blank=True, null=True)
    eventtime = models.CharField(max_length=4, verbose_name='발생시각', help_text='사건 발생시각의 시/분을 24시간제 형태로 입력(hhmm) ex. 0020', blank=True, null=True)

    weather = models.SmallIntegerField(choices=WEATHER, verbose_name='날씨', help_text='날씨', blank=True, null=True)
    eventlocation = models.CharField(max_length=80, verbose_name='발생장소', help_text='사건 발생장소', blank=True, null=True)

    actorid = models.ForeignKey(Actor, on_delete=models.SET_NULL, verbose_name='주체(體)', help_text='사건 주체', blank=True, null=True)
    actid = models.ForeignKey(Act, on_delete=models.SET_NULL, verbose_name='작용(用)', help_text='주체의 작용', blank=True, null=True)
    category = models.ForeignKey(ActCategory, on_delete=models.SET_NULL, verbose_name='범주', help_text='사건 범주', blank=True, null=True)
    eventmemo = models.TextField(verbose_name='역사메모', help_text='이 날짜에 있었던 역사적인 사건을 기술할 것', blank=True, null=True)

    luckmemo = models.TextField(verbose_name='길흉메모', help_text='길흉 상세메모', blank=True, null=True)

    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL1', help_text='외부 관련 URL 1', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)

    def __str__(self):
        return str(self.eventyear) + '- ' + self.title


class SajuEvent(models.Model):
    '''
    기    능 : SajuEvent 모델
    주의사항 : userid만 있으면 생성 가능
    '''

    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User ID(*)', help_text='대상 User ID')
    sajuid = models.ForeignKey(Saju, on_delete=models.SET_NULL, verbose_name='사주ID', help_text='대상 사주 ID(Null이면 사주 미등록 회원의 입력 정보)', blank=True, null=True)

    #title필드는 암호화를 시키는 과정에서 문자열이 길어질 수 있는데, 끝이 잘리면 복호화가 안되므로 TextField로 설정
    title = models.TextField(verbose_name='사건(또는 일과) 제목', help_text='사건을 특정할 수 있는 제목이나 하루 일과를 설명할 수 있는 문구 (암호화되므로 입력자 외에는 관리자를 포함하여 아무도 확인할 수 없습니다)')

    datekey = models.ForeignKey(TICalendar, on_delete=models.SET_NULL, verbose_name='만세력 연결', help_text='양력 연월일(YYYYMMDD ex. 19771213)을 정확히 아는 경우, 입력하면 만세력에 연결됨', blank=True, null=True)
    eventyear = models.CharField(max_length=4, verbose_name='발생연도', help_text='발생연도만 아는 경우, 4자리 숫자로 입력(YYYY)', blank=True, null=True)
    eventmonth = models.CharField(max_length=2, choices=MONTH12, verbose_name='발생월', help_text='발생연도/월만 아는 경우, 양력 발생월 선택', blank=True, null=True)
    eventday = models.CharField(max_length=2, choices=DAY31, verbose_name='발생일', help_text='발생연도/월/일을 아는 경우, 양력 발생일 선택', blank=True, null=True)
    eventtime = models.CharField(max_length=4, verbose_name='발생시각', help_text='사건 시각을 24시간제 형태로 입력(hhmm) ex. 2120', blank=True, null=True)

    yeargan = models.CharField(max_length=2, choices=GAN, verbose_name='연간', help_text='연간', blank=True, null=True)
    yearji = models.CharField(max_length=2, choices=JI, verbose_name='연지', help_text='연지', blank=True, null=True)
    monthgan = models.CharField(max_length=2, choices=GAN, verbose_name='월간', help_text='월간', blank=True, null=True)
    monthji = models.CharField(max_length=2, choices=JI, verbose_name='월지', help_text='월지', blank=True, null=True)
    daygan = models.CharField(max_length=2, choices=GAN, verbose_name='일간', help_text='일간', blank=True, null=True)
    dayji = models.CharField(max_length=2, choices=JI, verbose_name='일지', help_text='일지', blank=True, null=True)
    timegan = models.CharField(max_length=2, choices=GAN, verbose_name='시간', help_text='시간', blank=True, null=True)
    timeji = models.CharField(max_length=2, choices=JI, verbose_name='시지', help_text='시지', blank=True, null=True)

    weather = models.SmallIntegerField(choices=WEATHER, verbose_name='날씨', help_text='날씨', blank=True, null=True)
    eventlocation = models.CharField(max_length=80, verbose_name='발생장소', help_text='사건 발생장소', blank=True, null=True)

    daewoongan = models.CharField(max_length=2, choices=GAN, verbose_name='대운천간', help_text='발생 당시 대운을 아는 경우, 대운 천간 선택', blank=True, null=True)
    daewoonji = models.CharField(max_length=2, choices=JI, verbose_name='대운지지', help_text='발생 당시 대운을 아는 경우, 대운 지지 선택', blank=True, null=True)
    sewoongan = models.CharField(max_length=2, choices=GAN, verbose_name='세운천간', help_text='발생 당시 세운을 아는 경우, 세운 천간 선택(만세력에 연결되었으면 입력할 필요없습니다)', blank=True, null=True)
    sewoonji = models.CharField(max_length=2, choices=JI, verbose_name='세운지지', help_text='발생 당시 세운을 아는 경우, 세운 지지 선택(만세력에 연결되었으면 입력할 필요없습니다)', blank=True, null=True)

    actorid = models.ForeignKey(Actor, on_delete=models.SET_NULL, verbose_name='주체(體)', help_text='사건 주체', blank=True, null=True)
    actid = models.ForeignKey(Act, on_delete=models.SET_NULL, verbose_name='작용(用)', help_text='주체의 작용', blank=True, null=True)
    category = models.ForeignKey(ActCategory, on_delete=models.SET_NULL, verbose_name='범주', help_text='사건 범주', blank=True, null=True)
    eventmemo = models.TextField(verbose_name='사건 내용', help_text='육하원칙에 따른 구체적인 사건 내용 (암호화되므로 입력자 외에는 관리자를 포함하여 아무도 확인할 수 없습니다)')

    wealthindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='재물지수', help_text='재물 관련도')
    healthindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='건강지수', help_text='건강 관련도')
    jobindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='직장지수', help_text='직장/관운 관련도')
    relationindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='관계지수', help_text='인간관계 관련도')
    studyindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='학업지수', help_text='학업 관련도')
    honorindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='명예지수', help_text='명예 관련도')
    moveindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='이동지수', help_text='이동(여행/전직/부서이동 등) 관련도')
    outcomeindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='성과지수', help_text='성과(연구/예술작품/자녀교육 등) 관련도')
    goe = models.SmallIntegerField(choices=GOE64, verbose_name='괘', help_text='사건과 관련하여 얻은 괘', blank=True, null=True)
    donghyo = models.SmallIntegerField(choices=HYO6, verbose_name='동효', help_text='사건 관련 득괘 결과의 동효', blank=True,null=True)
    goe_expected = models.SmallIntegerField(choices=GOE64, verbose_name='예상하는 괘', help_text='사건과 관련하여 예상하는 주역괘', blank=True, null=True)
    donghyo_expected = models.SmallIntegerField(choices=HYO6, verbose_name='예상하는 동효', help_text='예상하는 주역괘의 동효', blank=True, null=True)

    luckmemo = models.TextField(verbose_name='길흉 메모', help_text='자신의 입장에서 구체적인 길흉의 내용 (암호화되므로 입력자 외에는 관리자를 포함하여 아무도 확인할 수 없습니다)', blank=True, null=True)
    note = models.TextField(verbose_name='기타 참고할 메모', help_text='사건과 관련하여 참고할 내용 (암호화되므로 입력자 외에는 관리자를 포함하여 아무도 확인할 수 없습니다)', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL', help_text='외부 관련 URL', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)


    # 이 이하는 page_processor.py에서 직접 암호화하므로 별도로 정의할 필요가 없으나, property 설정방법을 참고하는 차원에서 그냥 두었음
    #===========================================================================
    # #eventmemo는 암호화하여 저장
    # def _get_eventmemo(self):
    #     crypto = MyCrypto()
    #     return crypto.decrypt(self.eventmemo)

    # def _set_eventmemo(self, value):
    #     crypto = MyCrypto()
    #     self.eventmemo = crypto.encrypt(value)

    # safe_eventmemo = property(_get_eventmemo, _set_eventmemo)

    # #luckmemo는 암호화하여 저장
    # def _get_luckmemo(self):
    #     crypto = MyCrypto()
    #     return crypto.decrypt(self.luckmemo)

    # def _set_luckmemo(self, value):
    #     crypto = MyCrypto()
    #     self.luckmemo = crypto.encrypt(value)

    # safe_luckmemo = property(_get_luckmemo, _set_luckmemo)
    #===========================================================================

    def get_absolute_url(self):
        return reverse('machine:detail', args=[self.pk])    # /machine/detail/<pk> 형식으로 template에 주소 출력(machine/urls.py에 기술)

    def __str__(self):
        return str(self.userid.username) + '(' + str(self.datekey) + ')- ' + self.title


class Iching(models.Model):
    '''
    64괘
    '''

    goe_id = models.SmallIntegerField(choices=GOE64, verbose_name='괘번호(*)', help_text='괘 번호(1~64)')
    goe_name = models.CharField(max_length=30, verbose_name='괘명', help_text='괘명')

    hyo1 = models.CharField(max_length=1, choices=PLUS_MINUS, verbose_name='초효', help_text='음효이면 2, 양효이면 3')
    hyo2 = models.CharField(max_length=1, choices=PLUS_MINUS, verbose_name='이효', help_text='음효이면 2, 양효이면 3')
    hyo3 = models.CharField(max_length=1, choices=PLUS_MINUS, verbose_name='삼효', help_text='음효이면 2, 양효이면 3')
    hyo4 = models.CharField(max_length=1, choices=PLUS_MINUS, verbose_name='사효', help_text='음효이면 2, 양효이면 3')
    hyo5 = models.CharField(max_length=1, choices=PLUS_MINUS, verbose_name='오효', help_text='음효이면 2, 양효이면 3')
    hyo6 = models.CharField(max_length=1, choices=PLUS_MINUS, verbose_name='상효', help_text='음효이면 2, 양효이면 3')

    goesa = models.CharField(max_length=100, default='괘사 원문', verbose_name='괘사 원문', help_text='괘사 원문', blank=True, null=True)
    goesa_desc = models.TextField(default='괘사 설명', verbose_name='괘사 설명', help_text='괘사 설명', blank=True, null=True)
    goesa_mine = models.TextField(default='괘에 관한 TI 설명', verbose_name='괘사 설명', help_text='괘에 관한 TI 설명', blank=True, null=True)

    dansa = models.CharField(max_length=100, default='단사 원문', verbose_name='단사 원문', help_text='단사 원문', blank=True, null=True)
    dansa_desc = models.TextField(default='단사 설명', verbose_name='단사 설명', help_text='단사 설명', blank=True, null=True)
    dansa_mine = models.TextField(default='단사에 관한 TI 설명', verbose_name='단사 설명', help_text='단사에 관한 TI 설명', blank=True, null=True)

    hyosa1 = models.CharField(max_length=100, default='초효 효사 원문', verbose_name='초효 효사 원문', help_text='초효 효사 원문', blank=True, null=True)
    hyosa1_desc = models.TextField(default='초효 효사 설명', verbose_name='초효 효사 설명', help_text='초효 효사 설명', blank=True, null=True)
    hyosa1_mine = models.TextField(default='초효에 관한 TI 설명', verbose_name='초효 설명', help_text='초효에 관한 TI 설명', blank=True, null=True)

    hyosa2 = models.CharField(max_length=100, default='이효 효사 원문', verbose_name='이효 효사 원문', help_text='이효 효사 원문', blank=True, null=True)
    hyosa2_desc = models.TextField(default='이효 효사 설명', verbose_name='이효 효사 설명', help_text='이효 효사 설명', blank=True, null=True)
    hyosa2_mine = models.TextField(default='이효에 관한 TI 설명', verbose_name='이효 설명', help_text='이효에 관한 TI 설명', blank=True, null=True)

    hyosa3 = models.CharField(max_length=100, default='삼효 효사 원문', verbose_name='삼효 효사 원문', help_text='삼효 효사 원문', blank=True, null=True)
    hyosa3_desc = models.TextField(default='삼효 효사 설명', verbose_name='삼효 효사 설명', help_text='삼효 효사 설명', blank=True, null=True)
    hyosa3_mine = models.TextField(default='삼효에 관한 TI 설명', verbose_name='삼효 설명', help_text='삼효에 관한 TI 설명', blank=True, null=True)

    hyosa4 = models.CharField(max_length=100, default='사효 효사 원문', verbose_name='사효 효사 원문', help_text='사효 효사 원문', blank=True, null=True)
    hyosa4_desc = models.TextField(default='사효 효사 설명', verbose_name='사효 효사 설명', help_text='사효 효사 설명', blank=True, null=True)
    hyosa4_mine = models.TextField(default='사효에 관한 TI 설명', verbose_name='사효 설명', help_text='사효에 관한 TI 설명', blank=True, null=True)

    hyosa5 = models.CharField(max_length=100, default='오효 효사 원문', verbose_name='오효 효사 원문', help_text='오효 효사 원문', blank=True, null=True)
    hyosa5_desc = models.TextField(default='오효 효사 설명', verbose_name='오효 효사 설명', help_text='오효 효사 설명', blank=True, null=True)
    hyosa5_mine = models.TextField(default='오효에 관한 TI 설명', verbose_name='오효 설명', help_text='오효에 관한 TI 설명', blank=True, null=True)

    hyosa6 = models.CharField(max_length=100, default='상효 효사 원문', verbose_name='상효 효사 원문', help_text='상효 효사 원문', blank=True, null=True)
    hyosa6_desc = models.TextField(default='상효 효사 설명', verbose_name='상효 효사 설명', help_text='상효 효사 설명', blank=True, null=True)
    hyosa6_mine = models.TextField(default='상효에 관한 TI 설명', verbose_name='상효 설명', help_text='상효에 관한 TI 설명', blank=True, null=True)

    hyosa7 = models.CharField(max_length=100, default='추가효 효사 원문', verbose_name='추가효 효사 원문', help_text='추가효(용육/용구) 효사 원문', blank=True, null=True)
    hyosa7_desc = models.TextField(default='추가효 효사 설명', verbose_name='추가효 효사 설명', help_text='추가효(용육/용구) 효사 설명', blank=True, null=True)
    hyosa7_mine = models.TextField(default='추가효에 관한 TI 설명', verbose_name='추가효 설명', help_text='추가효(용육/용구)에 관한 TI 설명', blank=True, null=True)

    note = models.TextField(verbose_name='메모', help_text='괘에 관한 메모', blank=True, null=True)


    def __str__(self):
        return str(self.goe_id) + '- ' + self.goe_name


class IchingNote(models.Model):
    '''
    IchingNote
    '''

    title = models.CharField(max_length=80, verbose_name='노트 제목', help_text='노트 제목(ex. 백호살, 도화살, 춘목경금불가, 소강절본괘오행...)', blank=True, null=True) #admin에서 보기쉽게 관리하기 위한 필드
    theory = models.ForeignKey(Theory, on_delete=models.CASCADE, verbose_name='이론(*)', help_text='이론 명칭(ex. 백호살, 도화살, 춘목경금불가, 소강절본괘오행...)')   #하나의 이론을 설명하는 여러 레코드를 묶는 코드

    ####################################################################
    #이하 IchingCase 모델과 동일
    category = models.SmallIntegerField(default=0, choices=ICHINGSECTION, verbose_name='점단분류(*)', help_text='점단 카테고리 선택')
    goe = models.SmallIntegerField(choices=GOE64, verbose_name='괘(*)', help_text='점을 쳐서 얻은 괘')
    donghyo1 = models.BooleanField(default=False, verbose_name='초효동효여부(*)', help_text='초효가 동효인지 여부')
    donghyo2 = models.BooleanField(default=False, verbose_name='2효동효여부(*)', help_text='2효가 동효인지 여부')
    donghyo3 = models.BooleanField(default=False, verbose_name='3효동효여부(*)', help_text='3효가 동효인지 여부')
    donghyo4 = models.BooleanField(default=False, verbose_name='4효동효여부(*)', help_text='4효가 동효인지 여부')
    donghyo5 = models.BooleanField(default=False, verbose_name='5효동효여부(*)', help_text='5효가 동효인지 여부')
    donghyo6 = models.BooleanField(default=False, verbose_name='상효동효여부(*)', help_text='상효가 동효인지 여부')
    ####################################################################

    def __str__(self):
        return str(self.id) + '- ' + self.title


class IchingCase(models.Model):
    '''
    IchingCase
    '''

    userid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='User ID(*)', help_text='대상 User ID')
    sajuid = models.ForeignKey(Saju, on_delete=models.SET_NULL, verbose_name='사주ID', help_text='대상 사주 ID(Null이면 사주 미등록 회원의 입력 정보)', blank=True, null=True)

    datekey = models.ForeignKey(TICalendar, on_delete=models.SET_NULL, verbose_name='만세력 연결', help_text='양력 연월일(YYYYMMDD ex. 19771213)을 정확히 아는 경우, 입력하면 만세력에 연결됨', blank=True, null=True)
    ichingyear = models.CharField(max_length=4, verbose_name='점단연도', help_text='점단연도만 아는 경우, 4자리 숫자로 입력(YYYY)', blank=True, null=True)
    ichingmonth = models.CharField(max_length=2, choices=MONTH12, verbose_name='점단월', help_text='점단연도/점단월만 아는 경우, 양력 점단월 선택', blank=True, null=True)
    ichingday = models.CharField(max_length=2, choices=DAY31, verbose_name='점단일', help_text='점단연도/점단월/점단일을 아는 경우, 양력 점단일 선택', blank=True, null=True)
    ichingtime = models.CharField(max_length=4, verbose_name='점단시각', help_text='점단 시각을 24시간제 형태로 입력(hhmm) ex. 0020', blank=True, null=True)

    weather = models.SmallIntegerField(choices=WEATHER, verbose_name='날씨', help_text='날씨', blank=True, null=True)
    ichinglocation = models.CharField(max_length=80, verbose_name='점단장소', help_text='점을 친 장소', blank=True, null=True)

    actorid = models.ForeignKey(Actor, on_delete=models.SET_NULL, verbose_name='주체(體)', help_text='사건 주체', blank=True, null=True)
    actid = models.ForeignKey(Act, on_delete=models.SET_NULL, verbose_name='작용(用)', help_text='주체의 작용', blank=True, null=True)
    question = models.TextField(default='점치는 내용을 입력할 것', verbose_name='질문내용(*)', help_text='질문내용(암호화되므로 입력자 외에는 관리자를 포함하여 아무도 확인할 수 없음)')

    ####################################################################
    #이하 IchingNote 모델과 동일
    category = models.SmallIntegerField(default=0, choices=ICHINGSECTION, verbose_name='점단분류(*)', help_text='점단 카테고리 선택')
    goe = models.SmallIntegerField(choices=GOE64, verbose_name='괘(*)', help_text='점을 쳐서 얻은 괘')
    donghyo1 = models.BooleanField(default=False, verbose_name='초효동효여부(*)', help_text='초효가 동효인지 여부')
    donghyo2 = models.BooleanField(default=False, verbose_name='2효동효여부(*)', help_text='2효가 동효인지 여부')
    donghyo3 = models.BooleanField(default=False, verbose_name='3효동효여부(*)', help_text='3효가 동효인지 여부')
    donghyo4 = models.BooleanField(default=False, verbose_name='4효동효여부(*)', help_text='4효가 동효인지 여부')
    donghyo5 = models.BooleanField(default=False, verbose_name='5효동효여부(*)', help_text='5효가 동효인지 여부')
    donghyo6 = models.BooleanField(default=False, verbose_name='상효동효여부(*)', help_text='상효가 동효인지 여부')
    ####################################################################

    futureluckindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='예측길흉지수(*)', help_text='예측 길흉지수')
    futureluckmemo = models.TextField(verbose_name='예측길흉메모', help_text='예측길흉메모(암호화되므로 입력자 외에는 관리자를 포함하여 아무도 확인할 수 없음)', blank=True, null=True)
    resultluckindex = models.SmallIntegerField(default=0, choices=GRADE5, verbose_name='결과길흉지수', help_text='결과 길흉지수', blank=True, null=True)
    resultluckmemo = models.TextField(verbose_name='결과길흉메모', help_text='결과길흉메모(암호화되므로 입력자 외에는 관리자를 포함하여 아무도 확인할 수 없음)', blank=True, null=True)
    matchpercent = models.SmallIntegerField(verbose_name='부합도(%)', help_text='부합도(%)', blank=True, null=True)
    sourceid = models.ForeignKey(Source, on_delete=models.SET_NULL, verbose_name='출처', help_text='출처 정보', blank=True, null=True)
    sourcememo = models.TextField(verbose_name='출처메모', help_text='출처 메모', blank=True, null=True)
    createdtime = models.DateTimeField(auto_now_add=True, verbose_name='점단입력날짜', help_text='점단 정보가 시스템에 최초 입력된 날짜와 시간', blank=True, null=True)
    expiredtime = models.DateField(verbose_name='점단유효날짜', help_text='점단 예측의 유효기한 ex. 2016-12-13', blank=True, null=True)
    ispublic = models.BooleanField(default=False, verbose_name='공개여부(*)', help_text='공개점단으로 할 것인지 여부 설정(공개점단은 관리자만 수정/삭제할 수 있음)')
    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)
    tipedia = models.URLField(verbose_name='tipedia URL', help_text='tipedia URL', blank=True, null=True)
    url1 = models.URLField(verbose_name='관련 URL1', help_text='외부 관련 URL 1', blank=True, null=True)
    url2 = models.URLField(verbose_name='관련 URL2', help_text='외부 관련 URL 2', blank=True, null=True)
    url3 = models.URLField(verbose_name='관련 URL3', help_text='외부 관련 URL 3', blank=True, null=True)

    def __str__(self):
        return str(self.userid.username) + '- ' + self.question


class WebMonitor(models.Model):
    '''
    WebMonitor
    '''

    subject = models.CharField(max_length=80, default='모니터링 작업 명칭', verbose_name='모니터링 작업 명칭(*)', help_text='모니터링 작업 명칭 입력')
    active = models.BooleanField(default=True, verbose_name='작업 활성화 여부(*)', help_text='모니터링 작업이 활성화되었는 지 여부(체크되어 있으면 활성화)')
    targeturl = models.URLField(verbose_name='대상 URL(*)', help_text='모니터링할 URL(반드시 프로토콜(ex. "http://")을 함께 표시하고, GET방식 전송 데이터가 있다면 URL에 연결하여 표시할 것)')
    targeturlfinal = models.URLField(verbose_name='최종 대상 URL', help_text='최종적으로 모니터링할 URL(세션데이터를 얻은 이후에만 탐색할 수 있는 URL이 따로 있는 경우에 사용. targeturl이 로그인 페이지이고, targeturlfinal이 최종적으로 탐색해야할 페이지인 경우가 이에 해당함.)', blank=True, null=True)

    #sqlite에서 JSONFields를 지원하지 않음
    # headers = JSONField(verbose_name='Headers(JSON)', help_text='Header값으로 특별히 전달해야할 데이터(ex. csrf값을 넘길 때 referer 설정)가 있는 경우(따옴표에 주의하여 JSON형식으로 입력해야 함). ex. {"referer": "http://www.treeinsight.org/ti48/%EB%8B%AC%EB%A0%A5/"}', blank=True, null=True)
    # cookies = JSONField(verbose_name='Cookies(JSON)', help_text='Cookie값으로 특별히 전달해야할 데이터(ex. csrf값을 넘길 때 csrf 설정)가 있는 경우(따옴표에 주의하여 JSON형식으로 입력해야 함). ex. {"enwiki_session": "17ab96bd8ffbe8ca58a78657a918558"}', blank=True, null=True)
    # putdata = JSONField(verbose_name='PUT전송데이터(JSON)', help_text='PUT방식으로 전송할 데이터(따옴표에 주의하여 JSON형식으로 입력해야 함). ex. {"username": "bob", "email": "bob@bob.com"}', blank=True, null=True)
    # proxies = JSONField(verbose_name='Proxy URLs(JSON)', help_text='우회가 필요한 경우 Proxy URLs(따옴표에 주의하여 JSON형식으로 입력해야 함). ex. {"http" :"http://117.16.46.63:3128"}', blank=True, null=True) #현재 서버가 영국에 있으므로, 대상 URL이 외국 IP를 차단하는 경우에 Proxy가 필요함
    headers = models.TextField(verbose_name='Headers(Text type)', help_text='Header값으로 특별히 전달해야할 데이터(ex. csrf값을 넘길 때 referer 설정)가 있는 경우(따옴표에 주의하여 JSON형식으로 입력해야 함). ex. {"referer": "http://www.treeinsight.org/ti48/%EB%8B%AC%EB%A0%A5/"}', blank=True, null=True)
    cookies = models.TextField(verbose_name='Cookies(Text type)', help_text='Cookie값으로 특별히 전달해야할 데이터(ex. csrf값을 넘길 때 csrf 설정)가 있는 경우(따옴표에 주의하여 JSON형식으로 입력해야 함). ex. {"enwiki_session": "17ab96bd8ffbe8ca58a78657a918558"}', blank=True, null=True)
    putdata = models.TextField(verbose_name='PUT전송데이터(Text type)', help_text='PUT방식으로 전송할 데이터(따옴표에 주의하여 JSON형식으로 입력해야 함). ex. {"username": "bob", "email": "bob@bob.com"}', blank=True, null=True)
    proxies = models.TextField(verbose_name='Proxy URLs(Text type)', help_text='우회가 필요한 경우 Proxy URLs(따옴표에 주의하여 JSON형식으로 입력해야 함). ex. {"http" :"http://117.16.46.63:3128"}', blank=True, null=True) #현재 서버가 영국에 있으므로, 대상 URL이 외국 IP를 차단하는 경우에 Proxy가 필요함

    targettext = models.CharField(max_length=80, default='최초 검색 텍스트(문자열 또는 정규식)', verbose_name='1차 검색 텍스트(*)', help_text='대상 URL에서 1차로 검색할 텍스트(정규식 가능). ex. 대한민국 또는 class="ellipsis_g @[0-9]+-[0-9]+">.+<.+>')
    targettextfinal = models.CharField(max_length=80, default='최종 검색 텍스트(문자열 또는 정규식)', verbose_name='재검색할 텍스트', help_text='1차 검색한 텍스트 안에서 다시 검색할 텍스트(정규식 가능). ex. 민국 또는 >.+<', blank=True, null=True)
    searchresultnumber = models.SmallIntegerField(verbose_name='재검색할 결과 번호', help_text='1차 검색한 텍스트 결과에서 다시 검색하려는 경우, 몇번째 결과에서 검색할 것인지 결정(0부터 시작하며, 지정하지 않는 경우에는 각각 검색)', blank=True, null=True)
    timeout = models.SmallIntegerField(default=15, verbose_name='접속시 타임아웃(*)', help_text='접속시 타임아웃 시간. 단위는 초(second).')
    interval = models.SmallIntegerField(default=0, verbose_name='모니터링 주기(*)', help_text='모니터링 주기. 0이면 "주기없음", 1부터는 "시(Hour)".')
    lastcheckedtime = models.DateTimeField(verbose_name='마지막 모니터링한 시점', help_text='(Machine이 직접 관리) 가장 최근에 모니터링한 날짜와 시간', blank=True, null=True)
    ifexist = models.CharField(max_length=80, verbose_name='존재 메시지', help_text='대상 URL에서 검출할 텍스트 발견시 출력할 메시지', blank=True, null=True)
    ifnotexist = models.CharField(max_length=80, verbose_name='부존재 메시지', help_text='대상 URL에서 검출할 텍스트 미발견시 출력할 메시지', blank=True, null=True)
    iferror = models.CharField(max_length=80, verbose_name='에러 메시지', help_text='대상 URL 접속 중 에러 발생시 출력할 메시지', blank=True, null=True)
    sourcesave = models.BooleanField(default=True, verbose_name='페이지 소스 저장 여부(*)', help_text='검색대상 페이지의 소스를 DB에 저장할 것인지 여부(체크되어 있으면 저장)')
    note = models.TextField(verbose_name='비고', help_text='참고사항 기재', blank=True, null=True)

    def __str__(self):
        return self.subject + '(Active: ' + str(self.active) + ')'


class WebMonitorLog(models.Model):
    '''
    WebMonitorLog
    '''

    webmonitorid = models.ForeignKey(WebMonitor, on_delete=models.CASCADE, verbose_name='WebMonitorID(*)', help_text='Machine이 직접 관리하는 테이블')
    createdtime = models.DateTimeField(auto_now_add=True, verbose_name='로그입력시간', help_text='로그 정보가 시스템에 최초 입력된 날짜와 시간', blank=True, null=True)
    checkstatus = models.SmallIntegerField(default=2, choices=CHECKSTATUS3, verbose_name='대상 텍스트 발견 여부(*)', help_text='대상 URL에서 검출할 텍스트 발견하였는 지 여부 (1: 확인, 2: 미확인, 3: 에러)')
    result = models.TextField(verbose_name='1차 검색 결과', help_text='1차 검색 결과내용(정규식에 해당하는 결과가 다수일 경우, 엔터로 분리하여 표시)', blank=True, null=True)
    resultfinal = models.TextField(verbose_name='최종 검색 결과', help_text='최종 검색 결과내용(정규식에 해당하는 결과가 다수일 경우, 엔터로 분리하여 표시)', blank=True, null=True)
    sourcetext = models.TextField(verbose_name='페이지 소스', help_text='검색한 페이지 소스', blank=True, null=True)
    note = models.TextField(verbose_name='작업메시지', help_text='중요사항 메시지', blank=True, null=True)

    def __str__(self):
        return str(self.webmonitorid.subject) + '(체크시간: ' + str(self.createdtime) + ')(체크결과: ' + str(self.checkstatus) + ')'


class Message(models.Model):
    '''
    MessageBoard
    '''

    sender = models.CharField(max_length=80, default='메시지 생성자 입력', verbose_name='메시지 생성자(*)', help_text='메시지를 생성한 주체')
    createdtime = models.DateTimeField(auto_now_add=True, verbose_name='메시지 생성시간', help_text='메시지 정보가 시스템에 최초 입력된 날짜와 시간', blank=True, null=True)
    title = models.CharField(max_length=80, default='제목 입력', verbose_name='메시지 제목(*)', help_text='메시지 제목')
    msg = models.TextField(verbose_name='메시지 내용', help_text='메시지 내용', blank=True, null=True)
    notified = models.BooleanField(default=False, verbose_name='통지 여부(*)', help_text='통지 되었는 지 여부(체크되어 있으면 통지한 것임)')
    notifier = models.CharField(max_length=40, verbose_name='통지수단', help_text='통지에 사용된 수단(ex. telegram, email ...)', blank=True, null=True)
    lastnotifiedtime = models.DateTimeField(verbose_name='마지막 통지 시점', help_text='(Machine이 직접 관리) 가장 최근에 통지한 날짜와 시간', blank=True, null=True)
    note = models.TextField(verbose_name='비고', help_text='참고사항', blank=True, null=True)

    def __str__(self):
        return self.title + ' (통지여부:' + str(self.notified) + ')'


class Registry(models.Model):
    '''
    Registry for Machine
    '''

    telegramchatid = models.CharField(max_length=80, verbose_name='보고용 텔레그램 채팅룸 ID', help_text='(Machine이 직접 관리) 각종 보고가 이루어지는 텔레그램 채팅룸 ID', blank=True, null=True)

    def __str__(self):
        return '[' + str(self.id) + '] TreeInsight Machine Registry'

