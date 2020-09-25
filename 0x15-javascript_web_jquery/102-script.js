document.addEventListener('DOMContentLoaded', function () {
  $('#btn_translate').click(function () {
    $.get('https://fourtonfish.com/hellosalut/?lang=' +
		$('#language_code').val(), (data) =>
      $('#hello').html(data.hello));
  });
});
