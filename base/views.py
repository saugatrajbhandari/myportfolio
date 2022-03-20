from email import message
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render
from django.urls import reverse 
from django.contrib import messages

from .models import Project, Skill, Message, Endorsement
from .forms import ProjectForm, MessageForm, SkillForm, EndorsementForm, CommentForm, QuestionForm


def homePage(request):
    projects = Project.objects.all()
    form = MessageForm()
    skills = Skill.objects.exclude(body='')
    other_skills = Skill.objects.filter(body='')
    endorsements = Endorsement.objects.filter(approved=True) 
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message is successfully sent.')
            return redirect('/')
    return render(request, 'base/home.html', {'projects': projects, 'skills':skills, 'other_skills': other_skills, 'form': form, 'endorsements':endorsements})


def projectPage(request, pk):
    project = Project.objects.get(pk=pk)
    count = project.comment.all().count()
    comments = project.comment.all().order_by('-created')
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.projects = project
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment is successfully added')
        form = CommentForm()
    context = {'project': project, 'count': count, 'comments': comments, 'form': form}
    return render(request, 'base/project.html', context)


def createProject(request):
    form = ProjectForm()
    if request.method=="POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    return render(request, 'base/project_form.html', context={'form':form})


def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    return render(request, 'base/project_form.html', context={'form':form})


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unreadCount = Message.objects.filter(is_read=False).count()
    context = {'inbox': inbox, 'unreadCount': unreadCount}
    return render(request, 'base/inbox.html', context)


def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    context = {'message': message}
    return render(request, 'base/message.html', context)


def addSkill(request):
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(request.POST)
        form.save()
        messages.add_message(request, messages.SUCCESS, 'new skill added.')
        return redirect(reverse('home'))
    context = {'form': form}
    return render(request, 'base/skill_form.html', context)


def addEndorsement(request):
    form = EndorsementForm()
    if request.method == "POST":
        form = EndorsementForm(request.POST)
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Thank you, your endorsement is successfully added!')
        return redirect(reverse('home'))
    context = {'form': form}
    return render(request, 'base/endorsement_form.html', context)


def chartPage(request):
    form = QuestionForm()
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'base/chart.html', {'form': form})