// a JavaScript script that updates the text color of the <header> element to red

const ul = $('.my_list');
const div = $('#add_item');
div.on('click', () => {
  ul.append('<li>Item</li>');
});
