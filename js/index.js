var animation = bodymovin.loadAnimation({
	container: document.getElementById('logo'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: 'data.json'
});

var domAnimationList = document.getElementsByClassName("animation");
var i = 0;
var fnAnimation = function (el, ms) {
	setTimeout(function () {
		el.classList.remove("animation");
	}, ms);
}

for (i = 0; i < domAnimationList.length; i++) {
	var el = domAnimationList.item(i);
	fnAnimation(el, i * 250);
}