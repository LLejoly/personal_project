/* 
========================================================================================
This file depends on others Javascript files.
To work with this file several files must be loaded before:
- request.js
- utils.js

This file is used to build html tables with JSON object given.
========================================================================================
 */

var beautifulHeader = {
    "box_num": "box number",
    "type_id": "type identification",
    "type_name_en": "name",
    "type_name_fr": "nom",
    "freezer_id": "freezer identification",
    "freezer_name": "freezer name",
    "number_boxes": "number of boxes",
    "date_formatted_in": "date in",
    "date_formatted_out": "date out",
    "product_name": "name",
    "text_descr": "product description",
    "period": "period (months)",
    "quantity": "quantity (in terms of person)",
    "prod_num": "product identification in the freezer",
    "prod_id": "product identification in the DB"

}

// apply the tablesorter script on the tables generated
$.myjQuery = function (id) {
    $(id).tablesorter();
};

//check the period in months between the current date and a date given
// and a integer that represent the number of months. Return flase if the 
// number is outdated.
function checkPeriod(date_in, period) {
    var date1 = new Date(date_in);
    var date2 = new Date();
    var timeDiff = Math.abs(date2.getTime() - date1.getTime());
    var diffMonths = Math.ceil(timeDiff / (1000 * 3600 * 24 * 30));
    if (diffMonths > period) {
        return false;
    }
    return true;
}
// This function is used to generate 
function generateTableFromJson(content) {
    var contentData = content['content'];
    // Extracts value form the html header
    var col = [];
    for (var i = 0; i < contentData.length; i++) {
        for (var key in contentData[i]) {
            if (col.indexOf(key) === -1) {
                col.push(key);
            }
        }
    }

    // Creation of a dynamic table
    var table = document.createElement("table");
    table.setAttribute("id", content['elementId'] + "_table");
    table.setAttribute("class", "tablesorter tablesorter-bootstrap table-responsive table-hover table-responsive-md");

    // Html header row based on information collected above
    var header = table.createTHead();
    // Table row
    var tr = header.insertRow(-1);

    for (var i = 0; i < col.length; i++) {
        // Table header
        var th = document.createElement("th");
        th.setAttribute("class", "text-center")
        if (beautifulHeader.hasOwnProperty(col[i]))
            th.innerHTML = beautifulHeader[col[i]];
        else
            th.innerHTML = col[i];
        tr.appendChild(th);
    }

    var body = table.createTBody();
    // ADD JSON DATA TO THE TABLE AS ROWS.
    for (var i = 0; i < contentData.length; i++) {

        tr = body.insertRow(-1);

        for (var j = 0; j < col.length; j++) {
            var tabCell = tr.insertCell(-1);
            tabCell.innerHTML = contentData[i][col[j]];
            // allows to check the period with the input date and the period
            // only applied when date_formatted_in, period and daet_formatted_out are present.
            if (contentData[i]['date_formatted_in'] && contentData[i]['period'] && contentData[i]['date_formatted_out'] == null) {
                if (!checkPeriod(contentData[i]['date_formatted_in'], contentData[i]['period'])) {
                    tr.style.backgroundColor = "orange";
                }
            }
        }
    }

    // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
    var divContainer = document.getElementById(content['elementId']);
    divContainer.innerHTML = "";
    divContainer.appendChild(table);

    // Call jquery function
    $.myjQuery("#" + content['elementId'] + "_table");
}

// Create a radio button
// group: specify the button group
// val: scpecify the value given to the radio button
// text: specify the text to display
// checked: specify if by default the button must be checked
function createRadioButton(group, val, text, checked) {
    if (checked == true) {
        return '<input type="radio" name="' + group + '" value="' + val + '" checked="checked">' + text + '<br>';
    } else {
        return '<input type="radio" name="' + group + '" value="' + val + '">' + text + '<br>';
    }

}
// Generate the product tables based on the parameters given from the product_selection form.
function setProductsTable() {
    var option1 = document.forms["product_selection"]["group1"].value;
    var option2 = document.forms["product_selection"]["group2"].value;
    productsObject = {
        type: "GET",
        url: domainUrl + "get_product/" + option1 + "/" + option2 + "/" + token,
        elementId: "products_table"
    };
    ajaxRequest(productsObject, generateTableFromJson);
}
// Generate the product_selection form
function generateProductSelection(objectIdentifier) {
    var f = document.createElement("form");
    f.setAttribute('method', 'POST');
    f.setAttribute('name', 'product_selection');
    f.setAttribute('action', 'javascript:void(0);');
    f.setAttribute("onsubmit", "setProductsTable()");

    var params = ['all', 'inside', 'outside'];
    var grp1 = "";
    var grp2 = "";

    for (var i = 0; i < params.length; i++) {
        if (i == 0) {
            grp1 += createRadioButton("group1", params[i], params[i], true);
        } else {
            grp1 += createRadioButton("group1", params[i], params[i], false);
        }
    }

    grp2 += createRadioButton("group2", 0, "all freezers", true);

    for (var i = 0; i < freezersObject.content.length; i++) {
        grp2 += createRadioButton("group2", freezersObject.content[i]['freezer_id'], freezersObject.content[i]['freezer_name'], false);
    }

    f.innerHTML = grp1 + "<hr>" + grp2;
    var x = document.createElement("INPUT");
    x.setAttribute("type", "submit");
    x.setAttribute("class", "btn btn-primary");
    f.appendChild(x);
    document.getElementById(objectIdentifier.toString()).appendChild(f);
}