/* 
========================================================================================
This file is used to achieve Ajax requests
========================================================================================
 */

// This functions allows to achieved  Ajax request
// We have:
// - callback: the callback function name that will be called after
// the execution of the ajax request.
// - objContent is a JSON object  that need to have
// some fields.
// at least:
// - type: with the method used. If the method is different from GET you should also have
// a field ToSend that contains a json object
// - url: That specify the url  on which we apply the request
// If we want to use the cascode callback additional fields need to be specified:
// - cascadeCallback: specify the callback is a cascade callback,
// - callbakc: That specify the name of the cascade callback
// - callbackParams: specify the eventual parameters needed by the cascade callback
//
function ajaxRequest(objContent, callback) {
    var xmlhttp = new XMLHttpRequest();
    var type = objContent['type'];

    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 0) {
            alert("unable to reach the server. Probably shut down");
        } else if (this.readyState == 4 && this.status == 200) {
            if (this.responseText.length > 0) {
                objContent['content'] = JSON.parse(this.responseText);
                if (objContent['cascadeCallback'] == true) {
                    objContent['callback'].call(this, objContent['callbackParams']);
                }
            } else {
                objContent['content'] = '';
            }
            callback(objContent);
        } else if (this.readyState == 4 && this.status >= 500) {
            alert('Impossible to establish a connection with the server');
        } else if (this.readyState == 4 && this.status == 404) {
            alert('The route of the request does not exist.');
        } else if (this.readyState == 4 && this.status == 400) {
            alert(this.responseText);
        }
    };
    xmlhttp.open(objContent['type'], objContent['url'], true);
    if (type == "POST" || type == "DELETE" || type == "PUT") {
        xmlhttp.setRequestHeader("Content-type", "application/json");
        xmlhttp.send(JSON.stringify(objContent['toSend']));
    } else {
        xmlhttp.send();
    }
}