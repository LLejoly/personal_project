// Set the freezer select menu in the 
// add product form. This function is called by the 
// an ajaxRequest and the content given is the result of 
// this request.
function updtSetFreezersIndexes(content) {
    var contentData = content['content'];
    var size = Object.keys(contentData).length;
    var arr = [];
    for (var i = 1; i <= size; i++) {
        var tmp = {};
        tmp["box_num"] = "box number " + i;
        tmp["id"] = i;
        tmp["index"] = contentData[i];
        arr.push(tmp);
    }
    content['content'] = arr;
    setSelectOption('box_id_updt_form', content, 'id', 'box_num');
}

function updtSetFreezerOptions(val) {
    updtObject = {
        type: "GET",
        url: domainUrl + "freezer_next_id/" + val + "/" + token,
    };
    ajaxRequest(updtObject, updtSetFreezersIndexes);
}

// Set the number linked to a freezer in the add product form
// use the addObject reference initialized in the file dashboard.html
function updtSetNumber(objIdentifier, val) {
    select = document.getElementById(objIdentifier);
    for (var i = 0; i < updtObject.content.length; i++) {
        if (updtObject.content[i]['id'] == val) {
            select.value = updtObject.content[i]['index'];
            break;
        }
    }
}