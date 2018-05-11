var animation = bodymovin.loadAnimation({
	container: document.getElementById('logo'),
	renderer: 'svg',
	loop: false,
	autoplay: true,
	path: 'logo.json'
});

var fnWindowResize = function () {

	var domPadding = document.getElementsByClassName("content-padding").item(0);
	var domLogo = document.getElementById("logo");

	domPadding.style.height = (parseFloat(getComputedStyle(domLogo)["top"]) - (parseFloat(getComputedStyle(domLogo)["height"]) / 2.0)) + "px";

}
animation.addEventListener('DOMLoaded', function () {
	fnWindowResize();
	window.addEventListener('resize', fnWindowResize, true);
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
});

$("form").submit(function(e){
    e.preventDefault();
    var formData = new FormData();
    var email = $('#email').val();

    formData.append('email', email );
    $.ajax({
          url: "/api/v1/subscribe/addList"
        , data: formData
        , processData: false
        , contentType: false
        , dataType: "HTML"
        , type: 'POST'
        , success: function(data, textStatus, xhr){
            if (xhr.status == 200){
                alert("Thank you for your supporting!");
                $('#email').reset();
            } else if (xhr.status == 210){
                alert("You've already input! Thank you again!");
                $('#email').reset();
            } else {
                alert("There is an error on the site! Please contact to contact@ciceron.me");
            }
        }
        , error: function(xhr, ajaxOptions, thrownError){
            alert("There is an error on the site! Please contact to contact@ciceron.me");
        }
    });
});
