if (document.documentElement.clientHeight < document.getElementById("main").clientHeight) {
	document.getElementById("right_float").style.height = document.getElementById("main").clientHeight + "px"
	document.getElementById("left_float").style.height = document.getElementById("main").clientHeight + "px"
}
else {
	document.getElementById("right_float").style.height = (document.documentElement.clientHeight * 1) + "px"
	document.getElementById("left_float").style.height = (document.documentElement.clientHeight * 1) + "px"
}
