from django.shortcuts import render, get_object_or_404

from django_ajax.decorators import ajax

from campaigns.models import Campaign, Session, Thread, Event

def index(request):
    return render(request, 'index.html')

def campaign(request, cid):
    campaign = Campaign.objects.get(pk=cid)
    if request.user != campaign.owner:
        return render(request, 'index.html')

    threads = campaign.thread_set.all()
    sessions = campaign.session_set.all()
    events = campaign.event_set.all()

    context = {
        'campaign': campaign,
        'threads': threads,
        'sessions': sessions,
    }

    session = request.GET.get('session')
    if session:
        context['selected_session'] = int(session)
        events = events.filter(session__pk=session)

    thread = request.GET.get('thread')
    if thread:
        context['selected_thread'] = int(thread)
        events = events.filter(threads__pk=thread)
    context['events'] = events

    return render(request, 'main.html', context)

@ajax
def save_event(request, eid):
    event = Event.objects.get(pk=eid)
    content = request.POST.get('content')
    event.content = content
    event.save()
    return content

