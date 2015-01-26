from django.shortcuts import render, get_object_or_404, redirect

from django_ajax.decorators import ajax

from campaigns.models import Campaign, Session, Event, Note

def index(request):
    return render(request, 'index.html')

def campaign(request, cid):
    try:
        campaign = Campaign.objects.get(pk=cid)
    except:
        return redirect('/')
    if request.user != campaign.owner:
        return redirect('/')

    sessions = campaign.session_set.all()
    events = campaign.event_set.all()

    context = {
        'campaign': campaign,
        'sessions': sessions,
    }

    session = request.GET.get('session')
    if session:
        context['selected_session'] = int(session)
        events = events.filter(session__pk=session)
    context['events'] = events.order_by('order')

    return render(request, 'events.html', context)

def notes(request, cid):
    try:
        campaign = Campaign.objects.get(pk=cid)
    except:
        return redirect('/')
    if request.user != campaign.owner:
        return redirect('/')

    sessions = campaign.session_set.all()
    events = campaign.event_set.all()
    notes = campaign.note_set.all()

    context = {
        'campaign': campaign,
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

    sid = request.POST.get('session')
    try:
        session = Session.objects.get(pk=session)
    except:
        return None
    if session.campaign != event.campaign:
        return None

    content = request.POST.get('content')
    event.content = content
    event.session = session
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
        s = c.session_set.order_by('number').last()
    ev = Event(campaign=c, session=s, content='New Event')
    ev.save()

    sessions = c.session_set.all()

    context = {
        'event': ev,
        'sessions': sessions,
    }

    return render(request, 'event.html', context)

@ajax
def event_up(request, eid):
    try:
        event = Event.objects.get(pk=eid)
    except:
        return None
    if request.user != event.campaign.owner:
        return None

    event.up()

@ajax
def event_down(request, eid):
    try:
        event = Event.objects.get(pk=eid)
    except:
        return None
    if request.user != event.campaign.owner:
        return None

    event.down()

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

@ajax
def new_note(request, cid):
    try:
        campaign = Campaign.objects.get(pk=cid)
    except:
        return None
    if request.user != campaign.owner:
        return None

    note = Note(campaign=campaign, title='Unnamed Note', content='')
    note.save()

    return render(request, 'note.html', {'note': note})

@ajax
def save_note(request, nid):
    try:
        note = Note.objects.get(pk=nid)
    except:
        return None
    if request.user != note.campaign.owner:
        return None

    title = request.POST.get('title')
    content = request.POST.get('content')
    note.title = title
    note.content = content
    note.save()

@ajax
def delete_note(request, nid):
    try:
        note = Note.objects.get(pk=nid)
    except:
        return None
    if request.user != note.campaign.owner:
        return None

    note.delete()

@ajax
def new_session(request, cid):
    try:
        campaign = Campaign.objects.get(pk=cid)
    except:
        return None
    if request.user != campaign.owner:
        return None

    newNum = campaign.session_set.count() + 1

    session = Session(campaign=campaign, number = newNum)
    session.save()

    return render(request, 'session.html', {'session': session})

