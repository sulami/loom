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

