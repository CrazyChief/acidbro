$(document).ready(function () {
	var forEach=function(t,o,r){if("[object Object]"===Object.prototype.toString.call(t))for(var c in t)Object.prototype.hasOwnProperty.call(t,c)&&o.call(r,t[c],c,t);else for(var e=0,l=t.length;l>e;e++)o.call(r,t[e],e,t)};
	var hamburgers = document.querySelectorAll('.hamburger');
	if (hamburgers.length > 0) {
		forEach(hamburgers, function(hamburger) {
			hamburger.addEventListener('click', function() {
				this.classList.toggle('is-active');
				$('.menu-button-box').toggleClass('open');
			}, false);
		});
	}
	$('.menu-button-box .a').bind( "click", function() {
		var body = $("html, body");
		body.stop().animate({scrollTop:0}, 2000, 'swing', function() { });
	});
	$('.menu-button-box .s').bind( 'click', '.menu-button-box.open .s', function() {
		if($('.menu-button-box').hasClass('open')){
			$('#search').submit();
			} else {
			$('.menu-button-box').find(".hamburger").get(0).click();
		}
	});
	$(window).click(function() {
		$('.menu-button-box').removeClass('open');
		$('.hamburger').removeClass('is-active');
	});
	$('.menu-button-box').on('click', function(e){
		e.stopPropagation();
		if (e.target !== this){
			return;
		}
		$(this).find(".hamburger").get(0).click();
	});
	$('#s-clear').on('click', function() {
		$('#search input').val('');
	});

	$('body').scroll(function(){
		var sticky = $('.menu-button-box'),
		scroll = $('body').scrollTop();

		if (scroll >= 150) sticky.addClass('scroll');
		else sticky.removeClass('scroll');
	});




	$('.project-slide').slick({
		//autoplay: true,
        autoplaySpeed: 4000,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        dots: true
	});
	$('.tsm-slide').slick({
		//autoplay: true,
        autoplaySpeed: 4000,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: true,
        dots: true
	});

	$slickMobile = false;
    function mobSlider(){
        if($(window).width() < 860){
            if(!$slickMobile){
                $(".news-all").slick({
                    dots: true,
                    arrows: true,
                    slidesToShow: 1,
					slidesToScroll: 1,
					infinite: false,
				});
                $slickMobile = true;
			}
			} else if($(window).width() > 860){
			if($slickMobile){
				$('.news-all').slick('unslick');
				$slickMobile = false;
			}
		}
	};
	mobSlider();
	$(window).on('resize', function(){
		mobSlider();
	});
	$('.resume-but').on('click', function(e){
		$('#submit').modalBox({
			'width':'90%'
		});
		return false;
	})
	$('#submit .m-close').on('click', function(e){
		$('#submit').modalBox('close');
		return false;
	})
	//scrollbar
	//jQuery('.table-content .wrapper').scrollbar();

	//vacancies
	$(document).on('click', '.careers-item .name', function(){
		if($(window).width() > 800){
			$(this).parent('.careers-item').toggleClass('open').find('.carrier-descr').slideToggle('slow');
		}
	})
	$(document).on('click', '.careers-title', function(){
		if($(window).width() <= 800){
			$(this).toggleClass('open').next('.careers-toggle').slideToggle('slow');
		}
	})
	// if($('.careers-left').length){
	// 	var fixmeTop = $('.careers-right').offset().top - 50;
	// 	var fixmebottom = $('footer').offset().top - $(window).height() + 100;
	// 	$('body').scroll(function() {
	// 		var currentScroll = $('body').scrollTop();
	// 		if (currentScroll > fixmebottom && $(window).width() > 1000) {
	// 			$('.careers-left').css({
	// 				position: 'absolute',
	// 				bottom: '100px',
	// 				top: 'auto'
	// 			});
	// 			} else if (currentScroll >= fixmeTop && $(window).width() > 1000) {
	// 			$('.careers-left').css({
	// 				position: 'fixed',
	// 				top: '50px'
	// 			});
	// 			} else {
	// 			$('.careers-left').css({
	// 				position: 'relative'
	// 			});
	// 		}
	// 	});
	// }


	//news slider
	$('.news-slide').slick({
		autoplay: true,
        autoplaySpeed: 4000,
        slidesToShow: 3,
        slidesToScroll: 1,
		arrows: true,
		dots: true,
		responsive: [
			{
				breakpoint: 940,
				settings: {
					slidesToShow: 2
				}
			},
			{
				breakpoint: 650,
				settings: {
					slidesToShow: 1
				}
			}
		]
	});

	//team slider
	$('.team-slide').slick({
		autoplay: true,
        autoplaySpeed: 4000,
        slidesToShow: 2,
        slidesToScroll: 1,
        arrows: true,
        dots: true,
		responsive: [
			{
				breakpoint: 805,
				settings: {
					slidesToShow: 1
				}
			}
		]
	});

	//progress bar
	if($('.facts-progress01').length){
		var bar01 = new ProgressBar.Circle('.facts-progress01', {
			strokeWidth: 6,
			easing: 'easeInOut',
			duration: 1500,
			color: '#0b319e',
			trailColor: '#d3e0fd',
			trailWidth: 6,
			svgStyle: null
		});
		$('.facts-progress01').waypoint(function(direction) {
			bar01.animate(1.0);
		},{context: 'body', offset:'50%'});
	}
	if($('.facts-progress02').length){
		var bar02 = new ProgressBar.Circle('.facts-progress02', {
			strokeWidth: 6,
			easing: 'easeInOut',
			duration: 3000,
			color: '#0b319e',
			trailColor: '#d3e0fd',
			trailWidth: 6,
			svgStyle: null
		});
		$('.facts-progress02').waypoint(function(direction) {
			bar02.animate(1.0);
		},{context: 'body', offset:'50%'});
	}
	if($('.facts-progress03').length){
		var bar03 = new ProgressBar.Circle('.facts-progress03', {
			strokeWidth: 6,
			easing: 'easeInOut',
			duration: 4500,
			color: '#0b319e',
			trailColor: '#d3e0fd',
			trailWidth: 6,
			svgStyle: null
		});
		$('.facts-progress03').waypoint(function(direction) {
			bar03.animate(1.0);
		},{context: 'body', offset:'50%'});
	}
	if($('.facts-progress04').length){
		var bar04 = new ProgressBar.Circle('.facts-progress04', {
			strokeWidth: 6,
			easing: 'easeInOut',
			duration: 6000,
			color: '#0b319e',
			trailColor: '#d3e0fd',
			trailWidth: 6,
			svgStyle: null
		});
		$('.facts-progress04').waypoint(function(direction) {
			bar04.animate(1.0);
		},{context: 'body', offset:'50%'});
	}
	if($('*[class^="fline"]').length){
		$('*[class^="fline"]').waypoint(function() {
			$('*[class^="fline"]').addClass('fly');
		},{context: 'body', offset:'50%'});
	}

	//tabs
	$(document).on('click','.tabs-list li:not(.active)', function () {
		$(this).addClass('active').siblings().removeClass('active')
		.closest('.tabs').find('.tabs-content').removeClass('active').eq($(this).index()).addClass('active');
	});

	//portfolio
	$(document).on('click', '.sector-img', function(){
		$(this).parent('.sector-item').toggleClass('open').find('.sector-descr').slideToggle('slow');
	})

	//calculator slider

	$('.calc-rent .calc-slide').on('init', function (event, slick, currentSlide, nextSlide) {
		window.countSlideRent = slick.slideCount;
	});
	$('.calc-build .calc-slide').on('init', function (event, slick, currentSlide, nextSlide) {
		window.countSlideBuild = slick.slideCount;
	});
	$('.calc-rent .calc-slide,.calc-build .calc-slide').slick({
		slidesToShow: 1,
		slidesToScroll: 1,
		arrows: true,
		dots: false
	});

	jQuery('.calc-rent .calc-slide').on('afterChange', function (event, slick, currentSlide, nextSlide) {
		var i = (currentSlide ? currentSlide : 0) + 1;
		$(".calc-rent .calc-slider").slider('value',i);
		checkIfStyleChanged('calc-rent');
	});
	jQuery('.calc-build .calc-slide').on('afterChange', function (event, slick, currentSlide, nextSlide) {
		var i = (currentSlide ? currentSlide : 0) + 1;
		$(".calc-build .calc-slider").slider('value',i);
		checkIfStyleChanged('calc-build');
	});
	$(".calc-build .calc-slider").slider({
		value: 1,
		min: 1,
		max: window.countSlideBuild,
		slide: function(event, ui) {
			$('.calc-build .calc-slide').slick('slickGoTo', ui.value - 1);
			checkIfStyleChanged('calc-build');
		}
	});
	$(".calc-rent .calc-slider").slider({
		value: 1,
		min: 1,
		max: window.countSlideRent,
		slide: function(event, ui) {
			$('.calc-rent .calc-slide').slick('slickGoTo', ui.value - 1);
			checkIfStyleChanged('calc-rent');
		}
	});
	$('.calc').slideToggle();
	$(document).on('click', '.more', function(){
		$(this).toggleClass('open');
		$(this).parent('.show-calc').find('.calc').slideToggle('slow');
		$('.calc-slide').slick('setPosition');
	});
	function checkIfStyleChanged(parentDiv) {
		if ($('.'+ parentDiv +' .ui-slider-handle').attr('data-originalstyle') != $('.'+ parentDiv +' .ui-slider-handle').attr('style')) {
			var $width =$('.'+ parentDiv +' .calc-slider').outerWidth() / 100;
			var $left = parseInt(parseInt($('.'+ parentDiv +" .ui-slider-handle").css("left"), 10) / $width);
			console.log($left)
			if($left == 100){
				$('.'+ parentDiv +' .ui-slider-handle').css('transform', 'translateX(-100%)');
			}
			else if($left == 0){
				$('.'+ parentDiv +' .ui-slider-handle').css('transform', 'none');
			}
			else{
				$('.'+ parentDiv +' .ui-slider-handle').css('transform', 'translateX(-50%)');
			}
		}
	}

	//animate div
	$('.replace-bounceInUp').waypoint(function(e) {
		$(this.element).addClass('bounceInUp');
	},{context: 'body', offset:'60%'});
	$('.replace-fadeInUp').waypoint(function(e) {
		$(this.element).addClass('fadeInUp');
	},{context: 'body', offset:'60%'});
	$('.replace-fadeInLeft').waypoint(function(e) {
		$(this.element).addClass('fadeInLeft');
	},{context: 'body', offset:'60%'});
	$('.replace-fadeInRight').waypoint(function(e) {
		$(this.element).addClass('fadeInRight');
	},{context: 'body', offset:'60%'});
	$('.replace-zoomIn').waypoint(function(e) {
		$(this.element).addClass('zoomIn');
	},{context: 'body', offset:'60%'});

	//animate svg
	if ($('#BuildTeam').length) {
		var c=$("#BuildTeam");c.load("http://45.55.132.244/reit/img/svg/BuildTeam.svg",b);
		function b(){
			TweenMax.to("#gear01", 4, {rotation:360, repeat:-1, transformOrigin:"50% 50%", ease:Linear.easeNone});
			TweenMax.to("#gear02", 4, {rotation:-360, repeat:-1, transformOrigin:"50% 50%", ease:Linear.easeNone});
			f = new TimelineMax({repeat:-1,repeatDelay:0.5});
			f.set("#coin",{autoAlpha:0})
			.to("#coin",0.7,{autoAlpha:1})
			.to("#coin",0.7,{y: 400})

		}
	}
	if ($('#YourIncome').length) {
		var c=$("#YourIncome");c.load("http://45.55.132.244/reit/img/svg/YourIncome.svg",b);
		function b(){
			f = new TimelineMax({repeat:-1});
			f.set("#coin01,#coin02,#coin03,#coin04,#coin05,#coin06",{x:1000})
			.to("#coin01",1,{x:-100},"coin")
			.to("#coin01",0.3,{delay:0.7,autoAlpha:0},"coin")
			.to("#coin02",1.1,{delay:0.3,x:-200},"coin")
			.to("#coin02",0.3,{delay:0.8,autoAlpha:0},"coin")
			.to("#coin03",1.3,{delay:0.5,x:-200},"coin")
			.to("#coin03",0.3,{delay:1.5,autoAlpha:0},"coin")
			.to("#coin04",1.1,{delay:0.6,x:-200},"coin")
			.to("#coin04",0.3,{delay:1.4,autoAlpha:0},"coin")
			.to("#coin05",1.1,{delay:0.8,x:-200},"coin")
			.to("#coin05",0.3,{delay:1.6,autoAlpha:0},"coin")
			.to("#coin06",1.1,{delay:0.5,x:-200},"coin")
			.to("#coin06",0.3,{delay:1.3,autoAlpha:0},"coin")

		}
	}
	if ($('#AttractPartners').length) {
		var c=$("#AttractPartners");c.load("http://45.55.132.244/reit/img/svg/AttractPartners.svg",b);
		function b(){
			f = new TimelineMax({repeat:-1});
			f.set("#chip01,#chip02,#chip03,#chip04,#chip05,#chip06,#chip07,#chip08,#chip09,#chip10,#chip11,#chip12,#chip13",{y:-500})
			.to("#chip01",1,{y:0},"chip")
			.to("#chip01",0.3,{delay:0.9,autoAlpha:0},"chip")
			.to("#chip02",1,{delay:0.2,y:0},"chip")
			.to("#chip02",0.3,{delay:1.1,autoAlpha:0},"chip")
			.to("#chip03",1,{delay:0.6,y:0},"chip")
			.to("#chip03",0.3,{delay:1.3,autoAlpha:0},"chip")
			.to("#chip04",1.2,{delay:0.6,y:0},"chip")
			.to("#chip04",0.3,{delay:1.5,autoAlpha:0},"chip")
			.to("#chip05",1,{delay:0.4,y:0},"chip")
			.to("#chip05",0.3,{delay:1.1,autoAlpha:0},"chip")
			.to("#chip06",1,{y:0},"chip")
			.to("#chip06",0.3,{delay:0.8,autoAlpha:0},"chip")
			.to("#chip07",1,{delay:0.3,y:0},"chip")
			.to("#chip07",0.3,{delay:1.2,autoAlpha:0},"chip")
			.to("#chip08",1.2,{delay:0.5,y:0},"chip")
			.to("#chip08",0.3,{delay:1.4,autoAlpha:0},"chip")
			.to("#chip09",1.1,{delay:0.7,y:0},"chip")
			.to("#chip09",0.3,{delay:1.6,autoAlpha:0},"chip")
			.to("#chip10",1.1,{delay:0.2,y:0},"chip")
			.to("#chip10",0.3,{delay:1,autoAlpha:0},"chip")
			.to("#chip11",0.7,{delay:0.4,y:0},"chip")
			.to("#chip11",0.3,{delay:0.8,autoAlpha:0},"chip")
			.to("#chip12",1.3,{delay:0.6,y:0},"chip")
			.to("#chip12",0.3,{delay:1.6,autoAlpha:0},"chip")
			.to("#chip13",0.9,{delay:0.5,y:0},"chip")
			.to("#chip13",0.3,{delay:1,autoAlpha:0},"chip")
		}
	}

	//img zoom
	(function($){

		// initialization
		Zoomify = function (element, options) {
			var that = this;

			this._zooming = false;
			this._zoomed  = false;
			this._timeout = null;
			this.$shadow  = null;
			this.$image   = $(element).addClass('zoomify');
			this.options  = $.extend({}, Zoomify.DEFAULTS, this.$image.data(), options);

			this.$image.on('click', function () { that.zoom(); });
			$(window).on('resize', function () { that.reposition(); });
			$(document).on('scroll', function () { that.reposition(); });
		};
		Zoomify.DEFAULTS = {
			duration: 200,
			easing:   'linear',
			scale:    0.9
		};

		// css utilities
		Zoomify.prototype.transition = function ($element, value) {
			$element.css({
				'-webkit-transition': value,
				'-moz-transition': value,
				'-ms-transition': value,
				'-o-transition': value,
				'transition': value
			});
		};
		Zoomify.prototype.addTransition = function ($element) {
			this.transition($element, 'all ' + this.options.duration + 'ms ' + this.options.easing);
		};
		Zoomify.prototype.removeTransition = function ($element, callback) {
			var that = this;

			clearTimeout(this._timeout);
			this._timeout = setTimeout(function () {
				that.transition($element, '');
				if ($.isFunction(callback)) callback.call(that);
			}, this.options.duration);
		};
		Zoomify.prototype.transform = function (value) {
			this.$image.css({
				'-webkit-transform': value,
				'-moz-transform': value,
				'-ms-transform': value,
				'-o-transform': value,
				'transform': value
			});
		};
		Zoomify.prototype.transformScaleAndTranslate = function (scale, translateX, translateY, callback) {
			this.addTransition(this.$image);
			this.transform('scale(' + scale + ') translate(' + translateX + 'px, ' + translateY + 'px)');
			this.removeTransition(this.$image, callback);
		};

		// zooming functions
		Zoomify.prototype.zoom = function () {
			if (this._zooming) return;

			if (this._zoomed) this.zoomOut();
			else this.zoomIn();
		};
		Zoomify.prototype.zoomIn = function () {
			var that      = this,
			transform = this.$image.css('transform');

			this.transition(this.$image, 'none');
			this.transform('none');

			var offset     = this.$image.offset(),
			width      = this.$image.outerWidth(),
			height     = this.$image.outerHeight(),
			nWidth     = this.$image[0].naturalWidth || +Infinity,
			nHeight    = this.$image[0].naturalHeight || +Infinity,
			wWidth     = $(window).width(),
			wHeight    = $(window).height(),
			scaleX     = Math.min(nWidth, wWidth * this.options.scale) / width,
			scaleY     = Math.min(nHeight, wHeight * this.options.scale) / height,
			scale      = Math.min(scaleX, scaleY),
			translateX = (-offset.left + (wWidth - width) / 2) / scale,
			translateY = (-offset.top + (wHeight - height) / 2 + $(document).scrollTop()) / scale;

			this.transform(transform);

			this._zooming = true;
			this.$image.addClass('zoomed').trigger('zoom-in.zoomify');
			setTimeout(function () {
				that.addShadow();
				that.transformScaleAndTranslate(scale, translateX, translateY, function () {
					that._zooming = false;
					that.$image.trigger('zoom-in-complete.zoomify');
				});
				that._zoomed = true;
			});
		};
		Zoomify.prototype.zoomOut = function () {
			var that = this;

			this._zooming = true;
			this.$image.trigger('zoom-out.zoomify');
			this.transformScaleAndTranslate(1, 0, 0, function () {
				that._zooming = false;
				that.$image.removeClass('zoomed').trigger('zoom-out-complete.zoomify');
			});
			this.removeShadow();
			this._zoomed = false;
		};

		// page listener callbacks
		Zoomify.prototype.reposition = function () {
			if (this._zoomed) {
				this.transition(this.$image, 'none');
				this.zoomIn();
			}
		};

		// shadow background
		Zoomify.prototype.addShadow = function () {
			var that = this;
			if (this._zoomed) return;

			if (that.$shadow) that.$shadow.remove();
			this.$shadow = $('<div class="zoomify-shadow"></div>');
			$('body').append(this.$shadow);
			this.addTransition(this.$shadow);
			this.$shadow.on('click', function () { that.zoomOut(); })

			setTimeout(function () { that.$shadow.addClass('zoomed'); }, 10);
		};
		Zoomify.prototype.removeShadow = function () {
			var that = this;
			if (!this.$shadow) return;

			this.addTransition(this.$shadow);
			this.$shadow.removeClass('zoomed');
			this.$image.one('zoom-out-complete.zoomify', function () {
				if (that.$shadow) that.$shadow.remove();
				that.$shadow = null;
			});
		};

		// plugin definition
		$.fn.zoomify = function (option) {
			return this.each(function () {
				var $this   = $(this),
				zoomify = $this.data('zoomify');

				if (!zoomify) $this.data('zoomify', (zoomify = new Zoomify(this, typeof option == 'object' && option)));
				if (typeof option == 'string' && ['zoom', 'zoomIn', 'zoomOut', 'reposition'].indexOf(option) >= 0) zoomify[option]();
			});
		};

	})(jQuery);
	$('.sertificate img').zoomify();
})
