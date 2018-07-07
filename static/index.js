if (input != 'none') {
	var picture = document.getElementById("picture");
	picture.innerHTML = '';
	var img = document.createElement("img");
	img.setAttribute("src","static/upload.jpg");
	/*img.setAttribute("src","https://test-machine-learning.herokuapp.com/images");*/
	picture.appendChild(img);
	var finding = document.getElementById("finding");
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
		var node = document.createElement("iframe");
		node.setAttribute("src","https://en.wikipedia.org/wiki/" + flower)
		node.setAttribute("style","height: 400px; width: 100%")
		finding.appendChild(node);
	}
};

