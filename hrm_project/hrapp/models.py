from django.db import models
import uuid

# User Table
class User(models.Model):
    # Fields
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique User ID", editable=False)
    username = models.CharField(max_length=30, help_text="Enter username")
    password = models.CharField(max_length=30, help_text="Enter password")
    company_email = models.EmailField(help_text="Enter company email")

    # Metadata
    class Meta:
        ordering = ['username']

    # Methods
    def get_aboslute_url(self):
        return reverse('user-detail-view', args=[str(self.user_id)])

    def __str__(self):
        return self.username

# Department Table
class Department(models.Model):
    dep_name = models.CharField(max_length=50, help_text="Enter department name")
    dep_description = models.CharField(max_length=200, help_text="Enter department description", blank=True, null=True)

    class Meta:
        ordering = ['dep_name']

    def get_asbsolute_url(self):
        return reverse('department-detail', args=[str(self.id)])

    def __str__(self):
        return self.dep_name
        
# Position Table
class Position(models.Model):
    position_name = models.CharField(max_length=50, help_text="Enter position name")
    pos_description = models.CharField(max_length=200, help_text="Enter position description", blank=True, null=True)

    class Meta:
        ordering = ['position_name']

    def get_asbsolute_url(self):
        return reverse('position-detail', args=[str(self.id)])

    def __str__(self):
        return self.position_name

# Employee Table
class Employee(models.Model):
    # Personal Information
    employee_id = models.AutoField(primary_key=True, editable=False)
    first_name = models.CharField(max_length=30, help_text="Enter employee first name")
    middle_name = models.CharField(max_length=30, help_text="Enter employee middle name") 
    last_name = models.CharField(max_length=30, help_text="Enter employee last name")
    date_of_birth = models.DateField(help_text="Enter employee birthday")
    phone_number = models.CharField(max_length=13, help_text="Enter employee phone number", blank=True, null=True)
    address = models.CharField(max_length=100, help_text="Enter employee address", blank=True, null=True)
    personal_email = models.EmailField(help_text="Enter employee personal email", blank=True, null=True)
    SEX_STATUS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    sex_status = models.CharField(
        max_length=1,
        choices=SEX_STATUS,
        blank=True,
        default='n',
        help_text='Sex'
    )

    # Employee Information
    join_date = models.DateField(blank=True, null=True)
    quit_date = models.DateField(blank=True, null=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True, help_text="Select department")
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, blank=True, null=True, help_text="Select position")
    salary = models.DecimalField(max_digits=14, decimal_places=2, blank=True, null=True, help_text="Enter Salary")
    username = models.ForeignKey('User', on_delete=models.SET_NULL, blank=True, null=True, help_text="Select username")
    image_url = models.CharField(max_length=300, blank=True, null=True, help_text="Enter image location")
    
    EMPLOYEE_STATUS = (
        ('w', 'Working'),
        ('i', 'Internship'),
        ('t', 'Temporarily off'),
        ('q', 'Quit job')
    )
    status = models.CharField(
        max_length=1,
        choices=EMPLOYEE_STATUS,
        blank=True,
        default='w',
        help_text='Employee status'
    )

    class Meta:
        ordering = ['first_name', 'department']
    
    def get_asbsolute_url(self):
        return reverse('employee-detail', args=[str(self.employee_id)])
        
    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
        
    def get_full_name(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'

# -------------------------------------------------------------------------------

# Create a new reocrd using the model's contructor
# record = MyModelName(username="Test Name",password="123",email="test@mail.com")

# Access model filed values using Python attributes
# print(record.id) # should return 1 for the first record
# print(record.username)
# print(record.password)
# print(record.email)

# Change record by modifying the fields, then calling save()
# record.username = "New name"

# Save the object into the database
# record.save()

# all_user = User.objects.all()
# Filter by format: field_name__match_type
# icontains (case insensitive)
# iexact (case-insensitive exact match)
# exact (case-sensitive exact)
# in, gt (greater than)
# startswith
# gmail_user = User.objects.filter(email__contains="gmail')
# number_gmail_users = gmail_user.count()
