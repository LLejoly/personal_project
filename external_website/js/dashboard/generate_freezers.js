function addFreezer(elementId) {
    console.log(document.getElementsByTagName('input'));
    console.log(document.forms[elementId].length);
    var length = document.forms[elementId].length;
    var data = document.forms[elementId].elements;
    var jsonData = {};
    for (i = 0; i < length; i++) {
        if (data[i].name != 'submit') {
            jsonData[data[i].name] = data[i].value;
        }
    }
    console.log(jsonData);

    ajaxRequest({ type: "POST", url: domainUrl + "freezers/" + token, elementId: "add_freezer", toSend: jsonData }, updateFreezerTable);
}

function updateFreezerTable(val) {
    ajaxRequest({type: "GET", url: domainUrl + "freezers/" + token, elementId: "freezers_table" }, generateTableFromJson);
}