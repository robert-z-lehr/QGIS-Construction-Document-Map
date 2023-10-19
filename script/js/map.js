// Attach an event listener to the DOMContentLoaded event.
// This ensures the script executes after the entire HTML document is loaded.
document.addEventListener("DOMContentLoaded", function() {
    try {
        // Initialize the map object using Leaflet.js.
        // Set the initial center of the map to Austin, TX, and the zoom level to 12.
        var map = L.map('map').setView([30.2762, -97.7431], 12);
        
        // LAYERS
        // Define the OpenStreetMap tile layer and its attribution.
        var osmLayer = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        });

        // Define the OpenTopoMap tile layer and its attribution.
        var topoLayer = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.opentopomap.org/">OpenTopoMap</a>'
        });

        // Define a black and white tile layer and its attribution.
        var bwLayer = L.tileLayer('https://tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
            attribution: '&copy; Wikimedia'
        });

        // Add the OpenStreetMap layer as the default layer when the map loads.
        osmLayer.addTo(map);

        // LAYER CONTROL
        // Layer control object that contains base layers
        var baseLayers = {
            "OpenStreetMap": osmLayer,
            "OpenTopoMap": topoLayer,
            "Black and White": bwLayer
        };

        // Add the layer control to the map, and place it on the top-right corner
        L.control.layers(baseLayers).addTo(map);

        // Listen for changes on all input elements with the name attribute set to 'layer'.
        document.querySelectorAll('input[name="layer"]').forEach((elem) => {
            // Attach a change event listener to each radio button.
            elem.addEventListener("change", function() {
                // Use a switch statement to handle the radio button value.
                switch (this.value) {
                    case 'osm':
                        // Remove other layers and add the OpenStreetMap layer.
                        map.removeLayer(topoLayer);
                        map.removeLayer(bwLayer);
                        map.addLayer(osmLayer);
                        break;
                    case 'topo':
                        // Remove other layers and add the OpenTopoMap layer.
                        map.removeLayer(osmLayer);
                        map.removeLayer(bwLayer);
                        map.addLayer(topoLayer);
                        break;
                    case 'bw':
                        // Remove other layers and add the black and white layer.
                        map.removeLayer(osmLayer);
                        map.removeLayer(topoLayer);
                        map.addLayer(bwLayer);
                        break;
                }
            });
        });
    
    // ERROR HANDLING
    } catch (e) {
        // Log any errors to the console.
        console.error("An error occurred while initializing the map: ", e);

        // Create a paragraph element to display an error message on the web page.
        var errorMessage = document.createElement("p");
        errorMessage.innerText = "If you're seeing this message, the map failed to load.";
        
        // Append the error message to the body of the HTML document.
        document.body.appendChild(errorMessage);
    }
});
