import os
import urllib
import mimetypes
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, Answer
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from member.models import User


def contact(request):
    now_page = request.GET.get('page', 1)
    question_list = Question.objects.order_by('-pub_date')
    p = Paginator(question_list, 10)
    info = p.get_page(now_page)
    start_page = (int(now_page) - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages

    context = {'info': info,
        'page_range' : range(start_page, end_page + 1)}
    return render(request, 'contact/contact.html', context)


def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        result=Question.objects.filter(subject__contains=search)
        return render(
                request,
                'contact/show.html',
                {'data':result, 
                'search':search}
            )


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question
    }
    return render(request, 'contact/contact_detail.html', context)


from .forms import AnswerForm
@login_required(login_url='member:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.username = request.user.username
            answer.save()
            return redirect('contact:detail', question_id=question.id)
    else:
        form = AnswerForm()
    
    context = {'question': question, 'form': form}
    
    return render(request, 'contact/contact_detail.html', context)


from .forms import QuestionForm
@login_required(login_url='member:login')
def upload3(request):
    user = User.objects.get(username = request.user.username)   
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
             
        if form.is_valid():
            uploadFile = form.save(commit=False)
            if uploadFile.file:        
                name = uploadFile.file.name 
                size = uploadFile.file.size                              
            uploadFile.pub_date = timezone.now()
            uploadFile.username = request.user.username
            uploadFile.save()
            user.save()
            return redirect('contact:list')
    else:
        form = QuestionForm()
    return render(
        request, 'contact/contact_form.html', {'form': form})


def update(request, question_id):
    question = Question.objects.get(id=question_id)
    if(question.username == request.user.username):
        if request.method == "POST":
            question.subject = request.POST['subject']
            question.content = request.POST['content']
            question.pub_date = timezone.now()
            
            question.save()
            return redirect('contact:list')
        else:
            question=Question()
            return render(request, 'contact/update.html', {'question':question})
    else :
        return render(request, 'contact/warning.html')


def delete(request, question_id):
    question = Question.objects.get(id=question_id)
    if(question.username == request.user.username):
        question.delete()
        return redirect('contact:list')
    return render(request, 'contact/warning.html')


def answer_delete(request,answer_id):
    comment = Answer.objects.get(id=answer_id)
    if(comment.username == request.user.username):
        comment.delete()
        return redirect('contact:list')
    return render(request, 'contact/warning.html')



def download(request,question_id):   
    question = get_object_or_404(Question, pk=question_id)
    if question.file:
        url = question.file.url[1:] 
        file_url = urllib.parse.unquote(url)
        if os.path.exists(file_url) :
            with open(file_url, 'rb') as fh:
                quote_file_url = urllib.parse.quote(file_url.encode('utf-8'))
                response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
                response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'%s' % quote_file_url
                return response
    else :  
        return render(request, 'contact/delete.html')
