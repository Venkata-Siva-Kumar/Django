from django.contrib import admin
from .models import Department ,Programme,Student,Course,GradeSheet

# Register your models here.

admin.site.register(Department);
admin.site.register(Programme);
admin.site.register(Student);
admin.site.register(Course);
admin.site.register(GradeSheet);

