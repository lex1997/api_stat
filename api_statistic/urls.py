from django.urls import path
from . import views

app_name = "api_statistic"

urlpatterns = [
    path(r"cases/", views.CaseList.as_view(), name="case_list"),
    path(r"cases/<int:pk>/", views.CaseDetail.as_view(), name="case_detail"),
]