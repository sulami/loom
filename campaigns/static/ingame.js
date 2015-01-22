/*
 * Send an event creation request to the server and add the
 * corrosponding elements to the page.
 */
function new_event(cid, sid) {
    ajaxGet('/'+cid+'/'+sid+'/new/', function(content) {
        $('#events').append("<div class='event'><textarea data-autoresize rows='1' spellcheck='false' class='content' onblur='save_event("+content+", this)'>New Event</textarea><div class='edit'><select id='session'></select><a id='delete' onClick='del_event(this, "+content+")'>delete</a></div></div>");
    })
};

/*
 * Save content from the textarea to the event object.
 */
function save_event(id, ev) {
    ajaxPost('/'+id+'/save/', {'content': $(ev).val() }, function(content) {
    })
};

/*
 * Send an event delete request to the server and delete the
 * corrosponding event div.
 */
function del_event(element, eid) {
    ajaxGet('/'+eid+'/del/', function(content) {
        $(element).parent().parent().remove();
    })
};

/*
 * Query the note content and throw it up on the screen.
 */
function open_note(nid) {
    ajaxGet('/note/'+nid+'/', function(content) {
        $('#notes').append(content);
    })
};

/*
 * Send the possibly updated note back to the server and close the note
 * window.
 */
function close_note() {
    $('#open_note').remove();
};

