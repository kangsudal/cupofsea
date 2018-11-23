from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm, SpeakingForm, ReadingForm

# Create your views here.
def index(request):
	postlist = Post.objects.all()
	return render(request, 'main/index.html', {'postlist':postlist})

def blog(request):
	postlist = Post.objects.all()
	return render(request, 'main/blog.html',{'postlist':postlist})

def postdetails(request, pk):
	postlist = Post.objects.get(pk=pk)	
	return render(request, 'main/postdetails.html', {'postlist':postlist})


def speaking_log(request):
	postlist = Post.objects.all()
	return render(request, 'main/speaking_log.html', {'postlist':postlist})	

def listening_log(request):
	postlist = Post.objects.all()
	return render(request, 'main/listening_log.html', {'postlist':postlist})	
	
def writing_log(request):
	form = SpeakingForm()#writingForm으롸꿔야함
	return render(request, 'main/writing_log.html', {'form':form})	

def reading_log(request):
	form = ReadingForm()

	return render(request, 'main/reading_log.html', {'form':form})


def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/')
    else:
        return render(request, 'template.html', {'timezones': pytz.common_timezones})	