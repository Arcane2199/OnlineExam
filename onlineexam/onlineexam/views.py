from django.shortcuts import render
from onlineexam.models Exam 

def examonline(request):
    results=Exam.objects.all()
    return render(request,'Index.html',{"Exam":results})