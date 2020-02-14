from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# No module named 'django.core.urlresolvers'
#from django.core.urlresolvers import reverse
from .forms import TopicForm,EntryForm
from .models import Topic,Entry

# Create your views here.
def index(request):
    """学习笔记的主页"""
    return render(request, 'myProjects/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'myProjects/topics.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, "entries": entries}
    return render(request, 'myProjects/topic.html', context)

def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        """未提交数据：创建一个新表单"""
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myProjects:topics'))
    
    context = {'form': form}
    return render(request, 'myProjects/new_topic.html', context)

def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('myProjects:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'myProjects/new_entry.html', context)

def edit_entry(request, entry_id):
    """编辑现有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myProjects:topic', args=[topic.id]))

    context = {'entry': entry, 'topic':topic, 'form': form}
    return render(request, 'myProjects/edit_entry.html', context)