/* 
========================================================================================
This file depends on others Javascript files.
To work with this file several files must be loaded before:
- request.js
- utils.js
- generate_table.js


This file is used to manage the update form of a product.
It allows to retrieve the values sent with this form and do the appropriate thing with these.
========================================================================================
 */

// Set the freezer select menu in the 
// update product form. This function is called by the 
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
// Notify that the update has been done correctly
function notifyUpdate() {
    // update the porducts table after the modifications made
    setProductsTable();
    document.getElementById("update_message").innerHTML = "The product is updated";
}
// Retrieves information of the update form and achieves the request
// to update an exisiting element and send the information to the database
function updateProduct() {
    // clean the element that  notify the update is a success
    document.getElementById("update_message").innerHTML = "";

    var length = document.forms["update_product"].length;
    var data = document.forms["update_product"].elements;
    var updtProduct = {};
    var freezer_id;
    var box_num;
    var prod_num;
    var prod_loc;
    for (i = 0; i < length; i++) {
        if (data[i].name == 'freezer_id_main') {
            freezer_id = data[i].value;
        } else if (data[i].name == 'box_num_id') {
            box_num = data[i].value;
        } else if (data[i].name == 'prod_num_id') {
            prod_num = data[i].value;
        } else if (data[i].name == 'prod_loc') {
            prod_loc = data[i].value;
        } else if (data[i].name != 'submit') {
            updtProduct[data[i].name] = data[i].value;
        }
    }
    //Send newProduct to ajaxRequest
    product = {
        type: "POST",
        url: domainUrl + "update_product/" + freezer_id + "/" + box_num + "/" + prod_num + "/" + prod_loc + "/" +
            token,
        toSend: updtProduct
    }
    ajaxRequest(product, notifyUpdate);
}