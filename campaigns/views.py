from django.shortcuts import render, get_object_or_404, redirect

from django_ajax.decorators import ajax

from campaigns.models import Campaign, Session, Thread, Event, Note

def index(request):
    return render(request, 'index.html')

def campaign(request, cid):
    try:
        campaign = Campaign.objects.get(pk=cid)
    except:
        return redirect('/')
    if request.user != campaign.owner:
        return redirect('/')

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
    try:
        campaign = Campaign.objects.get(pk=cid)
    except:
        return redirect('/')
    if request.user != campaign.owner:
        return redirect('/')

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
    try:
        event = Event.objects.get(pk=eid)
    except:
        return None
    if request.user != event.campaign.owner:
        return None

    content = request.POST.get('content')
    event.content = content
    event.save()

    return content

@ajax
def new_event(request, cid, sid):
    try:
        c = Campaign.objects.get(pk=cid)
    except:
        return None
    if request.user != c.owner:
        return None

    if sid != '0':
        try:
            s = Session.objects.get(pk=sid)
        except:
            return None
    else:
        lastevent = c.event_set.order_by('-time').last()
        s = lastevent.session
    ev = Event(campaign=c, session=s, content='New Event')
    ev.save()

    sessions = c.session_set.all()

    context = {
        'event': ev,
        'sessions': sessions,
    }

    return render(request, 'event.html', context)

@ajax
def delete_event(request, eid):
    try:
        event = Event.objects.get(pk=eid)
    except:
        return None
    if request.user != event.campaign.owner:
        return None

    event.delete()

@ajax
def note(request, nid):
    try:
        note = Note.objects.get(pk=nid)
    except:
        return None
    if request.user != note.campaign.owner:
        return None

    return render(request, 'note.html', {'note': note})

