function ajaxRequest(objContent, callback) {
    var xmlhttp = new XMLHttpRequest();
    var type = objContent['type'];

    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            if (this.responseText.length > 0) {
                objContent['content'] = JSON.parse(this.responseText);
            } else {
                objContent['content'] = '';
            }
            callback(objContent);
        }
        // need to manage other types exception
    };
    xmlhttp.open(objContent['type'], objContent['url'], true);
    if (type == "POST") {
        xmlhttp.setRequestHeader("Content-type", "application/json");
        xmlhttp.send(JSON.stringify(objContent['toSend']));
    } else {
        xmlhttp.send();
    }
}
