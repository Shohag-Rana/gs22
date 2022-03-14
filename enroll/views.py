from django.shortcuts import render
from . forms import StudentRegistration

# Create your views here.
def formvalidation(request):
    fm = StudentRegistration(auto_id= 'id_for_%s', label_suffix=' -->', initial={'name': 'shohag rana', 'mail':'mdshohag7613@gmail.com'})
    # print(fm.as_p())
    return render(request, 'enroll/formdetails.html', {'form': fm})
