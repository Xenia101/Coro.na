# Coro.na

A Web **Map** Service for the **Corona-virus**

Data : [질병관리본부](http://www.cdc.go.kr/index.es?sid=a2)

Map API : [Kakao Map](http://apis.map.kakao.com/)

## Execution / Test Environment

- Window 10
- Node.js **latest version**

## Example

```javascript
<script>
        var mapContainer = document.getElementById('map'),
            mapOption = { 
                center: new kakao.maps.LatLng(35.350375967591494, 127.86952137759117),
                minLevel: 12,
                maxLevel: 13,
                level: 13
            };
        var map = new kakao.maps.Map(mapContainer, mapOption); 

        var clusterer = new kakao.maps.MarkerClusterer({
            map: map,
            averageCenter: true, 
            minLevel: 10
        });
    
        $.getJSON("http://localhost:8080/location", function(data) {
            var markers = $(data.positions).map(function(i, position) {
                return new kakao.maps.Marker({
                    position : new kakao.maps.LatLng(position.lat, position.lng)
                });
            });
            clusterer.addMarkers(markers);
        });  
</script>
```

<p align=center>
  <img width="300px" src="https://github.com/Xenia101/Coro.na/blob/master/img/img4.PNG?raw=true">
  <img width="300px" src="https://github.com/Xenia101/Coro.na/blob/master/img/image.PNG?raw=true">
</p>


<p align=center>
  <img width="300px" src="https://github.com/Xenia101/Coro.na/blob/master/img/img2.PNG?raw=true">
  <img width="300px"src="https://github.com/Xenia101/Coro.na/blob/master/img/img3.PNG?raw=true">
</p>

> This image is of Republic of Korea, February 8, 2020.

## References

[질병관리본부](http://www.cdc.go.kr/index.es?sid=a2)

[Kakao Map](http://apis.map.kakao.com/)
