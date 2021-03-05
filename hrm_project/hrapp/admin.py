from django.contrib import admin

# Register your models here.
from .models import Employee, User, Department, Position

# admin.site.register(Employee)
# admin.site.register(User)
# admin.site.register(Department)
admin.site.site_header = 'Human Resource Management'
# -------------------------------------------------------

# Define the admin class
#class EmployeeAdmin(admin.ModelAdmin):
#    pass

# Register the admin class with the associated models
#admin.site.register(Employee, EmployeeAdmin)

@admin.register(Employee)
class Employee(admin.ModelAdmin):
    def display_status(self, obj):
        EMPLOYEE_STATUS = {
            'w': 'Working',
            'i': 'Internship',
            't': 'Temporarily off',
            'q': 'Quit job'
        }
        return EMPLOYEE_STATUS[obj.status]

    display_status.short_description = 'Status'
    
    list_display = ('first_name', 'middle_name', 'last_name', 'department','display_status')
    list_filter = ('status', 'department')
    fieldsets = (
        ('Personal Information', {
            'fields': (
                ('first_name', 'middle_name', 'last_name'),
                'date_of_birth',
                ('phone_number', 'address', 'personal_email'),
				'sex_status'
            )
        }),
        ('Employee Information', {
            'fields': (
                'image_url',
                ('join_date', 'quit_date'),
                ('department', 'position', 'salary'),
                'username',
                'status',
            )
        }),
    )
    
@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('username', 'company_email', )

@admin.register(Department)
class Department(admin.ModelAdmin):
    list_display = ('dep_name', )
    
@admin.register(Position)
class Position(admin.ModelAdmin):
    list_display = ('position_name', )