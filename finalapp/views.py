# from django.http import HttpResponse
from django.shortcuts import render
from .models import Department,Course
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404


from .models import  Course
# def demo(request, obj=None):
#
#         obj1=department.objects.all()
#         return render(request,'index.html',{'result':obj,'value':obj1})
def message(request):
    return render(request,'message.html')
def form(request):
    return render(request,'form.html')
    #    department_id = request.GET.get('department')
    #    courses = Course.objects.filter(department_id=department_id).order_by('name')
    #    # return render(request, 'hr/city_dropdown_list_options.html', {'courses':courses})
    #    return render(request, 'form.html', {'courses': courses})
def newpage(request):
    return render(request,'newpage.html')
def home(request):
    return render(request,'index.html')
# def person_create_view(request):
#     form = PersonCreationForm()
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('person_add')
#     return render(request, 'finalapp/hom.html', {'form': form})
#
#
# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             form.save()
#             return redirect('person_change', pk=pk)
#     return render(request, 'finalapp/hom.html', {'form': form})
#
#
# # AJAX
# def load_courses(request):
#     department_id = request.GET.get('department_id')
#     courses = Course.objects.filter(department_id=department_id).all()
#     return render(request, 'finalapp/course_dropdown_list_options.html', {'courses': courses})
#     # return JsonResponse(list(cities.values('id', 'name')), safe=False)
