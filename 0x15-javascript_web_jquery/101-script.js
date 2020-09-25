document.addEventListener('DOMContentLoaded', function () {
  $('#add_item').click(() => $('UL.my_list').append('<li>Item</li>'));
  // .eq(-1) sets to last item in JS array of UL.my_list LI tags
  // .remove() removes that item from the DOM
  $('#remove_item').click(() => $('UL.my_list LI').eq(-1).remove());
  $('#clear_list').click(() => $('UL.my_list').empty());
});
