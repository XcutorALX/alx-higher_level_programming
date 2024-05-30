// a JavaScript script that updates the text color of the <header> element to red

const header = $('header');
const div = $('#update_header');
div.on('click', () => {
  header.text('New Header!!!');
});
