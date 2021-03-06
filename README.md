# Coro.na

A Web **Map** Service for the **Corona-virus**

## Example

```html
<div id="map" class="main" style="height: 100vh"></div>
```

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

> This image is of Republic of Korea, *February 8, 2020*.

## Browser Support

| ![chrome](https://camo.githubusercontent.com/26846e979600799e9f4273d38bd9e5cb7bb8d6d0/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f6368726f6d652f6368726f6d655f34387834382e706e67) 	| ![Firefox Edge](https://camo.githubusercontent.com/6087557f69ec6585eb7f8d7bd7d9ecb6b7f51ba1/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f66697265666f782f66697265666f785f34387834382e706e67) 	| ![IE](https://camo.githubusercontent.com/4b062fb12353b0ef8420a72ddc3debf6b2ee5747/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f617263686976652f696e7465726e65742d6578706c6f7265725f392d31312f696e7465726e65742d6578706c6f7265725f392d31315f34387834382e706e67) 	| ![Safari](https://camo.githubusercontent.com/6fbaeb334b99e74ddd89190a42766ea3b4600d2c/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f7361666172692f7361666172695f34387834382e706e67) 	| ![Opera](https://camo.githubusercontent.com/96d2405a936da1fb8988db0c1d304d3db04b8a52/68747470733a2f2f7261772e6769746875622e636f6d2f616c7272612f62726f777365722d6c6f676f732f6d61737465722f7372632f6f706572612f6f706572615f34387834382e706e67) 	|
|:------:	|:------------:	|:--:	|:------:	|:-----:	|
|    ✔   	|       ✔      	|  ✔ 	|    ✔   	|   ✔   	|


## Execution / Test Environment

- Window 10
- Python **3.6**


## References

**Data** : [질병관리본부](http://www.cdc.go.kr/index.es?sid=a2)

**Map API** : [Kakao Map](http://apis.map.kakao.com/)
