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

$.myjQuery = function(id) {
    $(id).tablesorter();
 };

function generateTableFromJson(content) {
    var contentData = content['content'];
    // EXTRACT VALUE FOR HTML HEADER. 
    // ('Book ID', 'Book Name', 'Category' and 'Price')
    var col = [];
    for (var i = 0; i < contentData.length; i++) {
        for (var key in contentData[i]) {
            if (col.indexOf(key) === -1) {
                col.push(key);
            }
        }
    }

    // CREATE DYNAMIC TABLE.
    var table = document.createElement("table");
    table.setAttribute("id", content['elementId'] + "_table");
    table.setAttribute("class","tablesorter-bootstrap table-responsive table-hover table-responsive-md");

    // CREATE HTML TABLE HEADER ROW USING THE EXTRACTED HEADERS ABOVE.
    var header = table.createTHead();
    var tr = header.insertRow(-1);                   // TABLE ROW.

    for (var i = 0; i < col.length; i++) {
        var th = document.createElement("th");      // TABLE HEADER.
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
        }
    }

    // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.
    var divContainer = document.getElementById(content['elementId']);
    divContainer.innerHTML = "";
    divContainer.appendChild(table);

    //Call jquery function
    $.myjQuery("#" + content['elementId'] + "_table"); 
}