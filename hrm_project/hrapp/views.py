from django.shortcuts import render
from hrapp.models import Employee, Department, User, Position
from django.db.models import Q
from django.views import generic

from django.template.defaulttags import register

# Forms
# from .forms import EmployeeForm
# from django.http import HttpResponseRedirect

@register.filter
def get_range(value):
    return range(value)
	
@register.filter
def get_range_by_columns(value):
    return range(0,value,3)
	
@register.filter
def get_index(value):
    return value - 1

# ListView
class EmployeeListView(generic.ListView):
    model = Employee
    # own name for the list as a template variable
    context_object_name = 'employee_list'
    # get employees list
    queryset = Employee.objects.filter(Q(status__exact = 'w') | Q(status__exact = 'i') | Q(status__exact = 't'))
    # specify own template name/location
    template_name = "employee/employee_view.html"
    
    # overriding
    # def get_queryset(self):
        # return Employee.objects.filter(Q(status__exact = 'w') | Q(status__exact = 'i') | Q(status__exact = 't'))
        
    # def get_context_data(self, **kwargs):
        # call the base implementation first to get the context
        # context = super(EmployeeListView, self).get_context_data(**kwargs)
        # create any data ad add it to the context
        # context['data'] = 'value'
        # return context
        
# ListView
class DepartmentListView(generic.ListView):
    model = Department
    # own name for the list as a template variable
    context_object_name = 'department_list'
    # get department list
    queryset = Department.objects.filter()
    # specify own template name/location
    template_name = "department/department_view.html"
    
# ListView
class PositionListView(generic.ListView):
    model = Position
    # own name for the list as a template variable
    context_object_name = 'position_list'
    # get position list
    queryset = Position.objects.filter()
    # specify own template name/location
    template_name = "position/position_view.html"

# Create your views here.
def index(request):
    # Generate counts of some of the main objects
    num_employees = Employee.objects.all().count()
    num_users = User.objects.all().count()
    
    # Available employees (status = w and status = i)
    # Available employees (status = w and status = i and status = t)
    num_available_employees = Employee.objects.filter(Q(status__exact = 'w') | Q(status__exact = 'i')).count()
    num_working_employees = Employee.objects.filter(Q(status__exact = 'w') | Q(status__exact = 'i') | Q(status__exact = 't')).count()
    
    context = {
        'num_employees': num_employees,
        'num_users': num_users,
        'num_available_employees': num_available_employees,
        'num_working_employees': num_working_employees,
    }
    
    return render(request, 'index.html', context=context)