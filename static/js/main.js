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
  var failed = false;
  var failure_reason = '';
  $('.rsvp-answer-group').each(function() {
    // Verify that they chose attend/decline for each person.
    attending = $(this).find('.rsvp-options-yes').hasClass('active')
    declined = $(this).find('.rsvp-options-no').hasClass('active')
    if (!attending && !declined) {
      failed = true;
      failure_reason = 'You must select either "Attend" or "Decline" for each guest.';
      return;
    }
    // Verify that each attending guest has a meal choice.
    if (attending) {
      if ($(this).find('.choose').html().indexOf('choose...') > -1) {
	failed = true;
	failure_reason = 'You must select a meal for each attending guest.';
	return;
      }
    }
  });
  if (failed) {
    $("#failure").html(failure_reason);
    $("#failure").show();
  }
  return !failed;
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

	$('.rsvp-guest-meal .dropdown-menu li').click(function() {
		$(this).closest('.dropdown-menu').prev('.mealSelection').children('.choose').text($(this).text());
	});
});

