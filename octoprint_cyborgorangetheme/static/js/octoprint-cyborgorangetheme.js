$(function() {
    function CyborgOrangeThemePluginViewModel(parameters) {
        var self = this;

        $("body").eq(0).addClass("OctoPrintTheme-CyborgOrange")
        $("#settings_dialog").eq(0).addClass("Cyborgified_Settings")

        }	
		OCTOPRINT_VIEWMODELS.push([
        CyborgOrangeThemePluginViewModel,
		[]
		
    ]);
});