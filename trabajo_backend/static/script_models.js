function filterBy(type) {
    var currentUrl = window.location.href;
    
    // Parse the URL to extract existing parameters
    var urlParts = currentUrl.split('?');
    var baseUrl = urlParts[0];
    var queryParams = urlParts[1] ? urlParts[1].split('&') : [];
    
    // Check if 'filter' parameter already exists
    var filterIndex = queryParams.findIndex(param => param.startsWith('filter='));
    
    if (filterIndex !== -1) {
        // If 'filter' parameter exists, update it
        queryParams[filterIndex] = 'filter=' + type;
    } else {
        // If 'filter' parameter does not exist, add it
        queryParams.push('filter=' + type);
    }
    
    // Rebuild the URL with updated parameters
    var updatedUrl = baseUrl + '?' + queryParams.join('&');
    
    // Redirect to the updated URL
    window.location.href = updatedUrl;
}

function updateUrl() {
    var select = document.getElementById("mySelect");
    var selectedOption = select.options[select.selectedIndex];
    var currentUrl = window.location.href;
    var orderParam = selectedOption.value;
    
    // Parse the URL to extract existing parameters
    var urlParts = currentUrl.split('?');
    var baseUrl = urlParts[0];
    var queryParams = urlParts[1] ? urlParts[1].split('&') : [];
    
    // Check if 'order' parameter already exists
    var orderIndex = queryParams.findIndex(param => param.startsWith('order='));
    
    if (orderIndex !== -1) {
        // If 'order' parameter exists, update it
        queryParams[orderIndex] = 'order=' + orderParam;
    } else {
        // If 'order' parameter does not exist, add it
        queryParams.push('order=' + orderParam);
    }
    
    // Rebuild the URL with updated parameters
    var updatedUrl = baseUrl + '?' + queryParams.join('&');
    
    // Redirect to the updated URL
    window.location.href = updatedUrl;
}