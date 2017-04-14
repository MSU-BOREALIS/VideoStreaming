# eclipse-pi-http
A simple HTTP interface for the Eclipse Pi.

## Making Requests
A request can be made via a standard web browser or via curl or wget. For simplicity, this server is not true REST and all endpoints are GET.

By default, the HTTP server listens on port 8080 and for most Pis, the base URL will be `http://192.168.1.3:8080/`.


## Video Recording
The HTTP interface allows for starting and stopping video on-device video recording on the Eclipse Pi. 

### Get Video Recording Status

* **Endpoint**
	 /video
* **Example URL**
	http://192.168.1.3:8080/video
* **Response if video is currently recording**
	* **Code:** 200
	* **Content:** `{ "isRecording": true }` 
* **Response if video is currently NOT recording**
	* **Code:** 200
	* **Content:** `{ "isRecording": false }` 


### Start Video Recording

* **Endpoint**
	/video/start
* **Example URL**
	http://192.168.1.103:8080/video/start
* **Successful Response**
	*  **Code:** 200
	*  **Content:** `{ "success": true }`
* **Failure Response**
	* **Code:** 500
	* **Content:** `{ "success": false, "error": "Video recording is already active." }`


### Stop Video Recording

* **Endpoint**
	/video/stop
* **Example URL**
	http://192.168.1.103:8080/video/stop
* **Successful Response**
	*  **Code:** 200
	*  **Content:** `{ "success": true }`
* **Failure Response**
	* **Code:** 500
	* **Content:** `{ "success": false, "error": "Video recording not in process." }`
