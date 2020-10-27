(function($) {
	"use strict";
	var fullHeight = function() {
		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});
	};
	fullHeight();
	$('#sidebarCollapse').on('click', function () {
		$('#sidebar').toggleClass('active').trigger('classChange');;
	});
})(jQuery);
function editName(name) {
    $('#'+name).prop('readonly', false).focus();
};
$(window).resize(function() {	
	if($(window).width() > 700 && $(window).width() < 1200){
		$('#sidebar').addClass('active').trigger('classChange');;
	}
	else{
		$('#sidebar').removeClass('active').trigger('classChange');;
	}
});
$('#sidebar').on('classChange', function() {
	if($('#sidebar').hasClass('active')){
		$('#content').removeClass('openMenu');
	}
	else{
		$('#content').addClass('openMenu');
	}
});
$(document).ready(function () {
	$(document).on('click', '.close span', function () {
		$(this).closest('.section').hide('slow');
	})
	if($(window).width() <= 700){
		$('#sidebar').removeClass('active');
	}
	if($(window).width() >= 1200){
		$('#sidebar').removeClass('active');
	}	
})
