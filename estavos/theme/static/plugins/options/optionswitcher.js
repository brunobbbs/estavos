var OptionSwitcher = function () {

	return {        

		//option Switcher
		initOptionSwitcher: function() {    
			var panel = jQuery('.option-switcher');

			jQuery('.option-switcher-btn').click(function () {
				jQuery(this).hide(100);
				jQuery('.option-switcher').addClass('fadeInRight').removeClass('fadeOutRight').show();
			});

			jQuery('.theme-close').click(function () {
				jQuery('.option-switcher').removeClass('fadeInRight').addClass('fadeOutRight').hide(1000);
				jQuery('.option-switcher-btn').show(1000);
			});
			
			jQuery('.color-options li').click(function () {
				var color = jQuery(this).attr("data-color");
				var data_logo = jQuery(this).attr("data-logo");
				setColor(color, data_logo);
				jQuery('.color-options li').removeClass("theme-active");
				jQuery(this).addClass("theme-active");
			});

			var setColor = function (color, data_logo) {
				jQuery('#option_color').attr("href", "css/colors/" + color + ".css");
				if(data_logo == 'logo1'){
					jQuery('.navbar-brand img').attr("src", "img/logo2" + ".png");
				}
				else if(data_logo == 'logo2'){
					jQuery('.navbar-brand img').attr("src", "img/logo3" + ".png");
				}
				else if(data_logo == 'logo3'){
					jQuery('.navbar-brand img').attr("src", "img/logo4" + ".png");
				}
				else if(data_logo == 'default-logo'){
					jQuery('.navbar-brand img').attr("src", "img/logo" + ".png");
				}
			}

			//Boxed Layout
			jQuery('.boxed-layout-btn').click(function(){
				jQuery(this).addClass("active-switcher-btn");
				jQuery(".wide-layout-btn").removeClass("active-switcher-btn");
				jQuery("body").addClass("bodyColor wrapper default");
				jQuery(".bg-patern").css({"display":"block"});
			});
			jQuery('.wide-layout-btn').click(function(){
				jQuery(this).addClass("active-switcher-btn");
				jQuery(".boxed-layout-btn").removeClass("active-switcher-btn");
				jQuery("body").removeClass("bodyColor wrapper default");
				jQuery(".bg-patern").css({"display":"none"});
			});

			//Background option
			jQuery('.bg-patern li.pattern-default').click(function () {
				jQuery('.bg-patern li').removeClass("pattern-active");
				jQuery(".bg-patern li.pattern-default").addClass("pattern-active");
				jQuery("body").addClass("default")
					.removeClass("pattern-01 pattern-02 pattern-03 pattern-04 pattern-05 pattern-06 pattern-07");
			});
			jQuery('.bg-patern li.pattern1').click(function () {
				jQuery('.bg-patern li').removeClass("pattern-active");
				jQuery(".bg-patern li.pattern1").addClass("pattern-active");
				jQuery("body").addClass("pattern-01")
					.removeClass("default pattern-02 pattern-03 pattern-04 pattern-05 pattern-06 pattern-07");
			});
			jQuery('.bg-patern li.pattern2').click(function () {
				jQuery('.bg-patern li').removeClass("pattern-active");
				jQuery(".bg-patern li.pattern2").addClass("pattern-active");
				jQuery("body").addClass("pattern-02")
					.removeClass("default pattern-01 pattern-03 pattern-04 pattern-05 pattern-06 pattern-07");
			});
			jQuery('.bg-patern li.pattern3').click(function () {
				jQuery('.bg-patern li').removeClass("pattern-active");
				jQuery(".bg-patern li.pattern3").addClass("pattern-active");
				jQuery("body").addClass("pattern-03")
					.removeClass("default pattern-01 pattern-02 pattern-04 pattern-05 pattern-06 pattern-07");
			});
			jQuery('.bg-patern li.pattern4').click(function () {
				jQuery('.bg-patern li').removeClass("pattern-active");
				jQuery(".bg-patern li.pattern4").addClass("pattern-active");
				jQuery("body").addClass("pattern-04")
					.removeClass("default pattern-01 pattern-02 pattern-03 pattern-05 pattern-06 pattern-07");
			});
			jQuery('.bg-patern li.pattern5').click(function () {
				jQuery('.bg-patern li').removeClass("pattern-active");
				jQuery(".bg-patern li.pattern5").addClass("pattern-active");
				jQuery("body").addClass("pattern-05")
					.removeClass("default pattern-01 pattern-02 pattern-03 pattern-04 pattern-06 pattern-07");
			});
			jQuery('.bg-patern li.pattern6').click(function () {
				jQuery('.bg-patern li').removeClass("pattern-active");
				jQuery(".bg-patern li.pattern6").addClass("pattern-active");
				jQuery("body").addClass("pattern-06")
					.removeClass("default pattern-01 pattern-02 pattern-03 pattern-04 pattern-05 pattern-07");
			});
			jQuery('.bg-patern li.pattern7').click(function () {
				jQuery('.bg-patern li').removeClass("pattern-active");
				jQuery(".bg-patern li.pattern7").addClass("pattern-active");
				jQuery("body").addClass("pattern-07")
					.removeClass("default pattern-01 pattern-02 pattern-03 pattern-04 pattern-05 pattern-06");
			});

			//Header option
			jQuery('.fixed-header').click(function(){
				jQuery(this).addClass("active-switcher-btn");
				jQuery('.static-header').removeClass("active-switcher-btn");
				jQuery("body").removeClass("static");
			});
			jQuery('.static-header').click(function(){
				jQuery(this).addClass("active-switcher-btn");
				jQuery(".fixed-header").removeClass("active-switcher-btn");
				jQuery("body").addClass("static");
			});
		}
	};
}();