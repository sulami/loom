from django.shortcuts import render, get_object_or_404, redirect

from django_ajax.decorators import ajax

from campaigns.models import Campaign, Session, Thread, Event, Note

def index(request):
    return render(request, 'index.html')

def campaign(request, cid):
    campaign = Campaign.objects.get(pk=cid)
    if request.user != campaign.owner:
        return redirect('index')

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

    return render(request, 'campaign.html', context)

def notes(request, cid):
    campaign = Campaign.objects.get(pk=cid)
    threads = campaign.thread_set.all()
    sessions = campaign.session_set.all()
    events = campaign.event_set.all()
    notes = campaign.note_set.all()
    context = {
        'campaign': campaign,
        'threads': threads,
        'sessions': sessions,
        'notes': notes,
    }
    return render(request, 'notes.html', context)

@ajax
def save_event(request, eid):
    event = Event.objects.get(pk=eid)
    content = request.POST.get('content')
    event.content = content
    event.save()
    return content

@ajax
def new_event(request, cid, sid):
    c = Campaign.objects.get(pk=cid)
    if sid != '0':
        s = Session.objects.get(pk=sid)
    else:
        lastevent = c.event_set.order_by('-time').last()
        s = lastevent.session
    ev = Event(campaign=c, session=s, content='New Event')
    ev.save()
    return ev.pk

@ajax
def delete_event(request, eid):
    event = Event.objects.get(pk=eid)
    event.delete()

@ajax
def note(request, nid):
    note = Note.objects.get(pk=nid)
    return render(request, 'note.html', {'note': note})

