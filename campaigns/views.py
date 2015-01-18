from django.shortcuts import render, get_object_or_404
from campaigns.models import Campaign, Session, Thread, Event

def index(request):
    return render(request, 'main.html')

def campaign(request, cid):
    campaign = Campaign.objects.get(pk=cid)
    threads = campaign.thread_set.all()
    sessions = campaign.session_set.all()
    events = campaign.event_set.all()
    context = {
        'campaign': campaign,
        'threads': threads,
        'sessions': sessions,
        'events': events,
    }
    return render(request, 'main.html', context)

