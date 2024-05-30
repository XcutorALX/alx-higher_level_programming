// a JavaScript script that updates the text color of the <header> element to red

$(document).ready(() => {
  const div = $('#hello');
  $.getJSON('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
    div.text(data.hello);
  });
});
