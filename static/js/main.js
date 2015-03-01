function submit_token() {
  var token = $("#token").val();
  if (token.length != 6) {
    $("#failure").show();
  } else {
    $("#failure").hide();
    token = token.toUpperCase();
    window.location.assign('/rsvp/' + token);
  }
}

function validateRSVPForm() {
  console.log('submit!');
  return true;
}

$( document ).ready(function() {
	function updateAttendingOptions(attending, element) {
		if (attending) {
			element.text("Attending");
			parent = element.closest('.rsvp-guest-coming');
			meal = parent.next().next('.rsvp-guest-meal').addClass('show');
			meal.next().next('.rsvp-guest-dietary').addClass('show');
		} else {
			element.text("Attend");
			parent = element.closest('.rsvp-guest-coming');
			meal = parent.next().next('.rsvp-guest-meal').removeClass('show');
			meal.next().next('.rsvp-guest-dietary').removeClass('show');
		}
	}

	$('.rsvp-options-yes').click(function() {
		updateAttendingOptions(true, $(this));
		$(this).next('.rsvp-options-no').removeClass('active');
		$(this).closest('.rsvp-guest-coming').next('input').val(1);
	});
	$('.rsvp-options-no').click(function() {
		var attendElem = $(this).prev('.rsvp-options-yes').removeClass('active');
		updateAttendingOptions(false, attendElem);
		attendElem.closest('.rsvp-guest-coming').next('input').val(0);
	});

	$('.rsvp-guest-meal .dropdown-menu li a').click(function() {
		$(this).closest('.dropdown-menu').prev('.mealSelection').children('.choose').text($(this).text());
		var tabIndex = $(this).attr("tabIndex");
		$(this).closest('.rsvp-guest-meal').next('input').val(tabIndex);
		event.preventDefault();
	});
});

