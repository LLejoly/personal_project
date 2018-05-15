
function setSelectOption(objectIdentifier, obj, val, txt) {
    var select, i, option;
    select = document.getElementById(objectIdentifier);
    //Clean up the the html node
    var selectParentNode = select.parentNode;
    var newSelectObj = select.cloneNode(false); // Make a shallow copy
    selectParentNode.replaceChild(newSelectObj, select);
    select = newSelectObj;
    // Set the default choice
    option = document.createElement('option');
    option.setAttribute('disabled', 'disabled');
    option.setAttribute('selected', true);
    option.setAttribute('value', '');
    option.text = ' -- select an option -- ';
    select.add(option);
    //set the different options that are available
    for (var i = 0; i < obj.content.length; i++) {
        option = document.createElement('option');
        option.value = obj.content[i][val];
        option.text = obj.content[i][txt];
        select.add(option);
    }
}