// "DOMContentLoaded" event is fired when the HTML is completely loaded and parsed
document.addEventListener("DOMContentLoaded", function() {
    try {
    // Initialize the map and set its initial center and zoom level
    var map = L.map('map').setView([30.2762, -97.7431], 12);
  
    // Define multiple tile layers
  
    // OpenStreetMap Tile Layer
    var osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    });
  
    // Another tile layer, for example, OpenTopoMap
    var topoLayer = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.opentopomap.org/">OpenTopoMap</a>'
    });
  
    // Add OpenStreetMap layer to map as default layer
    osmLayer.addTo(map);
  
    // Layer control object that contains base layers
    var baseLayers = {
        "OpenStreetMap": osmLayer,
        "OpenTopoMap": topoLayer
    };
  
    // Add the layer control to the map, and place it on the top-right corner
    L.control.layers(baseLayers).addTo(map);
    } catch (e) {
        console.error("An error occurred while initializing the map: ", e);
    }
});
