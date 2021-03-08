from django.shortcuts import render

# Create your views here.

# 引入Student类
from .models import Student
# 引入JsonResponse模块
from django.http import JsonResponse

# 定义方法获取全部学生信息
def get_students(request):
    try:
        # obj_students = Student.object.all().values()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code':1, 'data':students})
    except Exception as e:
        return JsonResponse({'code':0, 'msg':"异常："+str(e)})
