/**
 * This script toggles the class of the <header> element when the user clicks
 * on the tag DIV#toggle_header
 * The <header> element will always have one class: red or green, never both
 * in the same time and never empty
 */
$('DIV#toggle_header').bind({
  click: function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  }
});
