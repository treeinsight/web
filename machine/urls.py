from django.urls import path, include
from django.contrib.auth import views as auth_views #import this
from . import views


app_name = 'machine'    # 이곳에 app_name을 기술하고, 프로젝트 urls.py의 앱으로 라우팅시키는 위치에서 namespace를 기술해야, reverse()함수 등 사용가능


urlpatterns = [
    path("register_event", views.SajuEventCreateView.as_view(), name="register"),
    path("list_event", views.SajuEventListView.as_view(), name="list"),
    path('detail/<int:pk>', views.SajuEventDetailView.as_view(), name="detail"),   # /machine/detail/<pk> 형식으로 template에 주소 출력(machine/models.py에 기술)
    path('update/<int:pk>/edit', views.SajuEventUpdateView.as_view(), name="update"),
    path('delete/<int:pk>', views.SajuEventDeleteView.as_view(), name="delete"),
]
