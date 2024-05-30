// a JavaScript script that updates the text color of the <header> element to red

const header = $('header');
const div = $('#red_header');
div.on('click', () => { header.addClass('red'); });
