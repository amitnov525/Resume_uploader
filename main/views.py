from django.shortcuts import render,redirect
from main.forms import ResumeForm
from django.views import View
from main.models import Resume

# Create your views here.
class ResumeView(View):
    def get(self,request):
        candidates=Resume.objects.all()
        form=ResumeForm()
        context={'form':form,'candidates':candidates}
        return render(request,'main/home.html',context)
    def post(self,request):
        form=ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        form=ResumeForm()
        context={'form':form}
        return render(request,'main/home.html',context)
class CandidateView(View):
    def get(self,request,id):
        candidate=Resume.objects.get(id=id)
        context={'candidate':candidate}
        return render(request,'main/candidate.html',context)


            
    