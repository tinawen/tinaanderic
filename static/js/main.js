function submit_token() {
  var token = $("#token").val();
  if (token.length != 6) {
    $("#failure").show();
  } else {
    $("#failure").hide();
    token = token.toUpperCase();
    window.location.replace('rsvp/' + token)
  }
}

$( document ).ready(function() {
	function updateAttendingOptions(attending, element) {
		if (attending) {
			element.text("Attending");
			parent = element.closest('.rsvp-guest-coming');
			meal = parent.next('.rsvp-guest-meal').addClass('show');
			meal.next('.rsvp-guest-dietary').addClass('show');
		} else {
			element.text("Attend");
			parent = element.closest('.rsvp-guest-coming');
			meal = parent.next('.rsvp-guest-meal').removeClass('show');
			meal.next('.rsvp-guest-dietary').removeClass('show');
		}
	}

	$('.rsvp-options-yes').click(function() {
		updateAttendingOptions(true, $(this));
		$(this).next('.rsvp-options-no').removeClass('active');
	});
	$('.rsvp-options-no').click(function() {
		var attendElem = $(this).prev('.rsvp-options-yes').removeClass('active');
		updateAttendingOptions(false, attendElem);
	});
});

