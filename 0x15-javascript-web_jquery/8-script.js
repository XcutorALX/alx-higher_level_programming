// a JavaScript script that updates the text color of the <header> element to red

const ul = $('#list_movies');
$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  const items = data.results;
  items.forEach((item) => { ul.append(`<li>${item.title}</li>`); });
});
