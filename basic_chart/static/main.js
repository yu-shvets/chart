/**
 * Created by macuser on 11/22/16.
 */

function initRegionSelector() {
  // look up select element with groups and attach our even handler
  // on field "change" event
  $('#region-selector').find('select').change(function(event){
    // get value of currently selected group option
    var region = $(this).val();

    if (region) {
      // set cookie with expiration date 1 year since now;
      // cookie creation function takes period in days
      Cookies.set('current_region', region, {'path': '/'});
    } else {
      // otherwise we delete the cookie
      Cookies.remove('current_region', {'path': '/'});
    }

    // and reload a page
    location.reload(true);

    return true;
  });
}


$(document).ready(function(){
    initRegionSelector();
});