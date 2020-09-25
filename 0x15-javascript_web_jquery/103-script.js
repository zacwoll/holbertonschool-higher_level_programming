document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=' +
		$('#language_code').val(), (data) =>
      $('#hello').html(data.hello));
  });
  $('#language_code').keydown((e) => {
    // jquery uses keydown to bind an event listener to a key
    // pass the key in as an arg to the function
    // use arg.which === 13 as 13 is the Enter key
    // thus if language_code receives a keydown event from key 13, run this
    // code
    if (e.which === 13) {
      $.get('https://fourtonfish.com/hellosalut/?lang=' +
			$('#language_code').val(), (data) =>
        $('#hello').html(data.hello));
    }
  });
});
