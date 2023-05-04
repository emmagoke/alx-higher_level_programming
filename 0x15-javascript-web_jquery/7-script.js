/**
 * This script  fetches the character name from this URL:
 * https://swapi-api.alx-tools.com/api/people/5/?format=json
 *   The name will be displayed in the HTML tag DIV#character
 */
$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    $('DIV#character').text(data.name);
  });
});
