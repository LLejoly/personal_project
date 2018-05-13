function globalTendency(objectIdentifier) {
        ajaxRequest({
            type: "GET",
            url: domainUrl + "get_custom_tendency/" + token,
            elementId: objectIdentifier
        }, generateTableFromJson);
}