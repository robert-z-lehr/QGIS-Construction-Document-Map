document.addEventListener("DOMContentLoaded", function() {
    const map = L.map('map').setView([37.7749, -122.4194], 13); // San Francisco example

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);
});
