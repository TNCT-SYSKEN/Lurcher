from django.shortcuts import render
from .forms import PageCreateForm

# Create your views here.
<<<<<<< Updated upstream
=======
def create(request) :
        return render(request, 'mainsite/add.html')

def add(request):
    form = PageCreateForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return render(request,'mainsite/form_success.html')
    #最初にこちらを通って、次にif文の中を通ります
    context = {
        'form': form
    }
    return render(request,'mainsite/ofukai_create.html',context)

def home(request):
    #指定ファイルの名前は調整してください
    return render(request,'ofukai_create.html')
>>>>>>> Stashed changes
