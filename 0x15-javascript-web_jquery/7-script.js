// a JavaScript script that updates the text color of the <header> element to red

const div = $('#character');
$.getJSON('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
  div.text(data.name);
});
