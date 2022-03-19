from email import message
from django.shortcuts import redirect, render
from django.urls import reverse 
from django.contrib import messages

from .models import Project, Skill, Message
from .forms import ProjectForm, MessageForm, SkillForm


def homePage(request):
    projects = Project.objects.all()
    form = MessageForm()
    skills = Skill.objects.exclude(body='')
    other_skills = Skill.objects.filter(body='')
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message is successfully sent.')
            return redirect('/')
    return render(request, 'base/home.html', {'projects': projects, 'skills':skills, 'other_skills': other_skills, 'form': form})


def projectPage(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project   }
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