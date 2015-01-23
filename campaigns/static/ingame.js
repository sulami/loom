/*
 * Send an event creation request to the server and add the
 * corrosponding elements to the page.
 */
function new_event(cid, sid) {
    ajaxGet('/new_event/'+cid+'/'+sid+'/', function(content) {
        $('#new_event').before(content);
    })
};

/*
 * Save content from the textarea to the event object.
 */
function save_event(id, ev) {
    ajaxPost('/save_event/'+id+'/', { 'content': $(ev).val() });
};

/*
 * Send an event delete request to the server and delete the
 * corrosponding event div.
 */
function del_event(element, eid) {
    ajaxGet('/del_event/'+eid+'/');
    $(element).parent().parent().remove();
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
 * Send a note creation request and add the new link
 */
function new_note(cid) {
    ajaxGet('/new_note/'+cid+'/', function(content) {
        $('#new_note').before(content);
    })
};

/*
 * Send the possibly updated note back to the server and close the note
 * window.
 */
function save_note() {
    ajaxPost('/save_note/'+$('#id').val()+'/',
             {
                'title': $('#title').val(),
                'content': $('#content').val()
             }
    );
    $('#open_note').remove();
};

/*
 * Send a deletion request to the server
 */
function del_note() {
    var id = $('#id').val()
    ajaxGet('/del_note/'+id+'/');
    $('#open_note').remove();
    $('a.note#'+id).remove();
};

