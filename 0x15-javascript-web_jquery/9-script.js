/**
 * This script fetches from https://fourtonfish.com/hellosalut/?lang=fr and
 * displays the value of hello from that fetch in the HTML tag DIV#hello.
 */
$.ajax({
  url: 'https://fourtonfish.com/hellosalut/?lang=fr',
  type: 'GET',
  /* headers: {'Access-Control-Allow-Origin': '*'}, */
  dataType: 'json'
}).done(function (data) {
  $('DIV#hello').text(data.hello);
});
