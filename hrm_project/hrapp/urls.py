from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/', views.EmployeeListView.as_view(), name='employee'),
    path('department/', views.DepartmentListView.as_view(), name='department'),
    path('position/', views.PositionListView.as_view(), name='position'),
]