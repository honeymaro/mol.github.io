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

function validateEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

$("form").submit(function(e){
    e.preventDefault();
    var formData = new FormData();
    var email = $('#email').val();
    if (!validateEmail(email)){
        alert("Please input valid email address :)");
        return;
    }

    formData.append('email', email );
    $.ajax({
          url: "/api/v1/subscribe/addList"
        , data: formData
        , processData: false
        , contentType: false
        , dataType: "HTML"
        , type: 'POST'
        , success: function(data){
            alert("Thank you for your supporting!");
            $('#email').reset();
          }
        , error: function(xhr, ajaxOptions, thrownError){
            alert("There is an error on the site! Please contact to contact@ciceron.me");
          }
    });
});
