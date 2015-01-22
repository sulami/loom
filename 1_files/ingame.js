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
    ajaxPost('/save_event/'+id+'/', {'content': $(ev).val() },
        function(content) {
    })
};

/*
 * Send an event delete request to the server and delete the
 * corrosponding event div.
 */
function del_event(element, eid) {
    ajaxGet('/del_event/'+eid+'/', function(content) {
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

