// function display() {
// 			var cn = document.getElementById('one').value;
// 			var param = "cname="+cn; // + means concatination
// 			var request = new XMLHttpRequest(); // here we created object
// 			request.onreadystatechange = checkCname; // whenever we r geting response I'm calling checkCname function
// 			request.open("POST",'http://127.0.0.1:8000/checkone/',true) // here we have to go
// 			request.setRequestHeader('Content-Type','application/x-www-form-urlencoded');
// 			request.send(param)// here we r passing string because of post

// 			function checkCname(){
// 				// if(request.readyState === 4){
// 				// 	var val = request.responseText;
// 				// 	var json_data = JSON.parse(val); //converting string (text) to json type
// 					// if(json_data.error == "Name is present"){
// 					// 	document.getElementById('one1').style.color = 'red'
// 					// 	document.getElementById('one1').innerText = json_data.error
// 					// }
// 				// 	else{
// 				// 		document.getElementById('one1').style.color = 'green'
// 				// 		document.getElementById('one1').innerText = json_data.msg

// 				// 	}
// 				// }
// 			}
// 		}