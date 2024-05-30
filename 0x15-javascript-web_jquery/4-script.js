// a JavaScript script that updates the text color of the <header> element to red

const header = $('header');
const div = $('#toggle_header');
div.on('click', () => {
  header.toggleClass('red green');
});
