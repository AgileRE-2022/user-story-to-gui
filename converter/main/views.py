from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserStoryForm

from .models import UserStory

#from xxxx import handle_uploaded_file masih imaginary

#def upload_file(request):
    #if request.method == 'POST':
	 #   form = UploadFileForm(request.POST, request.FILES)
	  #  if form.is_valid():
	   #    handle_uploaded_file(request.FILES)
		#   return HttpResponseRedirect('/success/url/')
	    #else:
	     #  form = UploadFileForm()
	    #return render(request, 'upload.html', {'form': form})

def index(request):
	#return HttpResponse("User Story to GUI Converter")
	#USobjects = UserStory.objects.all
	return render(request, 'index.html', {})
	
def newstory(request) :
	if request.method == 'POST':
		form = UserStoryForm(request.POST or None)
		if form.is_valid()
			form.save()
		return render(request, 'index.html', {})
	else:
	return render(request, 'index.html', {})
	

