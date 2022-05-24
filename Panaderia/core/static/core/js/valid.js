function iniciarMap() {
    var coord = { lat: -33.3677175, lng: -70.7023468 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 15,
        center: coord

    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}
