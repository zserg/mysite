from django.shortcuts import render, render_to_response

# Create your views here.

import markdown                                                                 
import notes.static as s
from django.http import HttpResponse, HttpResponseRedirect
import os
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django import forms
from django.db import models
from django.forms import ModelForm, Textarea
from datetime import datetime

num_of_preview_lines = 10


class Note:
    pass

def mk_filelist():
    os.chdir(s.NOTES_PATH)
    files = filter(os.path.isfile, os.listdir(s.NOTES_PATH))
    files = [os.path.join(s.NOTES_PATH, f) for f in files] # add path to each file
    files.sort(key=lambda x: os.path.getmtime(x))
    files.reverse()
    return files


#def login():
#  username = request.POST['username']
#  password = request.POST['password']
#  user = authenticate(username=username, password=password)
#  if user is not None:
#      if user.is_active:
#            login(request, user)
#            # Redirect to a success page.
#      else:
#          pass
#           # Return a 'disabled account' error message
#  else:
#      pass
#         # Return an 'invalid login' error message.

@login_required
def main(request):
    """Main listing."""
    notes = mk_filelist()
    paginator = Paginator(notes, 10)
    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        notes = paginator.page(page)
    except (InvalidPage, EmptyPage):
        notes = paginator.page(paginator.num_pages)
    
    page_of_notes = []
    NotesArray = [] 
    for f in notes:
        n = Note()
        n.full_path = f
        n.file_name = os.path.basename(f)
        lines = []
        myfile = open(f,"r")
        lines = myfile.readlines()

#        import pdb; pdb.set_trace()

        if len(lines):
           n.title = lines.pop(0)
        else:
           n.title = n.file_name

        if len(lines)>num_of_preview_lines:
           num = 10
        else:
           num = len(lines)
        s=''.join(lines[:num]) 
        n.body = markdown.markdown(unicode(s,"utf-8"))
            #n.body = markdown.markdown("yyhello")
        NotesArray.append(n)
   
    notes_q = len(NotesArray)
    return render_to_response("notes/index.html", dict(notes=NotesArray, cnt=notes_q))

def post(request, file_name='index'):
      full_file_path = s.NOTES_PATH+file_name
      f = open(full_file_path, 'r')
      result = s.PAGE_TEMPLATE % markdown.markdown(f.read().decode('utf-8'))
      f.close()
      return HttpResponse(result)



class PostNoteForm(forms.Form):
     subject = forms.CharField(required=False,max_length=100, 
                               initial=datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
     body    = forms.CharField(widget=forms.Textarea(attrs={'rows':"2"}))


def newnote(request):
     if request.method == 'POST': # If the form has been submitted...
         form = PostNoteForm(request.POST) # A form bound to the POST data
         if form.is_valid(): # All validation rules pass
             f_name = form.cleaned_data['subject']
             f=open(s.NOTES_PATH+f_name+".txt", 'w')
             f.write(form.cleaned_data['body'])
             f.close()
              
              # Process the data in form.cleaned_data
              # ...
             return HttpResponseRedirect('/notes/') # Redirect after POS
     else:
         form = PostNoteForm() # An unbound form

     return render(request, 'notes/newnote.html', {
                'form': form,
            })

