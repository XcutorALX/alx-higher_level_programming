// a JavaScript script that updates the text color of the <header> element to red

$(document).ready(() => {
  const ul = $('.my_list');
  const add = $('#add_item');
  const rem = $('#remove_item');
  const clr = $('#clear_list');

  add.on('click', () => { ul.append('<li>Item</li>'); });
  rem.on('click', () => { $('UL.my_list li:last').remove(); });
  clr.on('click', () => { ul.empty(); });
});
