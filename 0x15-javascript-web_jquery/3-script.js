/**
 * This Javascript script adds the class red to the <header> element when the
 * user clicks on the tag DIV#red_header
 */
$('DIV#red_header').bind({
  click: function () {
    $('header').addClass('red');
  }
});
