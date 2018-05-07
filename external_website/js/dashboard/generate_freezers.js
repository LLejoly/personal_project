// This function allows to add freezer with the Freezer
// API. When the freezer is added. The function update the freezer
// table with the new freezer added.
// elementId: Is the html id of the freezer table to update.
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

    ajaxRequest({
        type: "POST",
        url: domainUrl + "freezers/" + token,
        elementId: "add_freezer",
        toSend: jsonData
    }, updateFreezerTable);
}

function updateFreezer(elementId) {
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

    ajaxRequest({
            type: "PUT",
            url: domainUrl + "freezers/" + token,
            elementId: "update_freezer",
            toSend: jsonData
        },
        updateFreezerTable);
}

function removeFreezer(elementId) {
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

    ajaxRequest({
            type: "DELETE",
            url: domainUrl + "freezers/" + token,
            elementId: "remove_freezer",
            toSend: jsonData
        },
        updateFreezerTable);
}


function updateFreezerTable(val) {
    ajaxRequest({
        type: "GET",
        url: domainUrl + "freezers/" + token,
        elementId: "freezers_table"
    }, generateTableFromJson);
}