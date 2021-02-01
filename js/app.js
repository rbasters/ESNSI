// carte centrée sur la France (latitude et longitude) et niveau de zoom = 6
let carte = L.map('mapid').setView([47.6, 2.5], 6);

// gestion du fond de carte
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
}).addTo(carte);

// insertion du marqueur pour Angers (latitude = 47.47073700, longitude = -0.55247200)
let marker = L.marker([47.47073700, -0.55247200]);
// ajout à la carte
marker.addTo(carte);
// bulle avec texte
marker.bindTooltip('Angers', {
   direction: "top",
   permanent: true,
   offset: [-15,-15], // on décale un peu la bulle vers le haut et à gauche,
   opacity: 0.6 // semi transparente
}).openTooltip();