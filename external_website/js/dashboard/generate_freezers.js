/* 
========================================================================================
This file depends on others Javascript files.
To work with this file several files must be loaded before:
- request.js
- utils.js
- generate_table.js


This file is used to manage the freezer.
========================================================================================
 */

// This function allows to add freezer with the Freezer
// API. When the freezer is added. The function update the freezer
// table with the new freezer added.
// elementId: Is the html id of the freezer table to update.
function addFreezer(elementId) {
    var length = document.forms[elementId].length;
    var data = document.forms[elementId].elements;
    var jsonData = {};
    for (i = 0; i < length; i++) {
        if (data[i].name != 'submit') {
            jsonData[data[i].name] = data[i].value;
        }
    }

    ajaxRequest({
        type: "POST",
        url: domainUrl + "freezers/" + token,
        elementId: "add_freezer",
        toSend: jsonData
    }, updateFreezerTable);
}
//This function is used to update the html table that represents the different freezers
// elementId: It is an html element where the table list will be displayed.
function updateFreezer(elementId) {
    var length = document.forms[elementId].length;
    var data = document.forms[elementId].elements;
    var jsonData = {};
    for (i = 0; i < length; i++) {
        if (data[i].name != 'submit') {
            jsonData[data[i].name] = data[i].value;
        }
    }
    ajaxRequest({
            type: "PUT",
            url: domainUrl + "freezers/" + token,
            elementId: "update_freezer",
            toSend: jsonData
        },
        updateFreezerTable);
}
//This function is used to remove an existing freezer and to update the view of the freezer table.
// elementId: It is an html element where the table list will be displayed.
function removeFreezer(elementId) {
    var length = document.forms[elementId].length;
    var data = document.forms[elementId].elements;
    var jsonData = {};
    for (i = 0; i < length; i++) {
        if (data[i].name != 'submit') {
            jsonData[data[i].name] = data[i].value;
        }
    }
    ajaxRequest({
            type: "DELETE",
            url: domainUrl + "freezers/" + token,
            elementId: "remove_freezer",
            toSend: jsonData
        },
        updateFreezerTable);
}
// This function is used to obtain the list of freezers from the API
// and generate the output.
function updateFreezerTable(val) {
    ajaxRequest({
        type: "GET",
        url: domainUrl + "freezers/" + token,
        elementId: "freezers_table"
    }, generateTableFromJson);
}