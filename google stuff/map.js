

function getLocation() {
  if (navigator.geolocation) {navigator.geolocation.getCurrentPosition(position,error);} 
  else { 
    x.innerHTML = "Geolocation is not supported.";
  }
}
  function position(position) {
  const latitude = position.coords.latitude;
  const longitude = position.coords.longitude;
  x.innerHTML = "Latitude: " + latitude + 
  "<br>Longitude: " + longitude;
    
}

function error(error){
  switch(error.code) {
    case error.PERMISSION_DENIED:
      x.innerHTML = "User denied the request for Geolocation."
      break;
    case error.POSITION_UNAVAILABLE:
      x.innerHTML = "Location information is unavailable."
      break;
    case error.TIMEOUT:
      x.innerHTML = "The request to get user location timed out."
      break;
    case error.UNKNOWN_ERROR:
      x.innerHTML = "An unknown error occurred."
      break;
  }
}  
  