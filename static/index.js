/*if there is a prediction result, show picture and wiki page*/
if (input != 'none') {
	var picture = document.getElementById("picture");
	/*if previous picture exists, delete it first*/
	picture.innerHTML = '';
	var img = document.createElement("img");
	/*upload image*/
	img.setAttribute("src","static/upload.jpg");
	img.style.width = '200px';
	/*img.setAttribute("src","https://test-machine-learning.herokuapp.com/images");*/
	picture.appendChild(img);
	var finding = document.getElementById("finding");
	/*if prediction probability or confidence is low, less than 50%, show message instead of wiki page*/
	if (probability <= 0.5) {
		var node = document.createElement("p");
		var message1 = document.createElement('span')
		message1.setAttribute("style","font-size: 30px;")
		message1.textContent = "Hmm... I am kind of busy now, "
		node.appendChild(message1);

		var message2 = document.createElement('span')
		message2.setAttribute("style","font-size: 40px; color: red;")
		message2.textContent = "go ask your mom!"
		node.appendChild(message2);
		finding.appendChild(node);
	} else {
		/*embed an iframe to the site, and direct to wiki page of the predicted flower*/
		var node = document.createElement("iframe");
		node.setAttribute("src","https://en.wikipedia.org/wiki/" + flower)
		node.setAttribute("style","height: 400px; width: 100%")
		finding.appendChild(node);
	}
};

