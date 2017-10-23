# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class CyborgOrangeThemePlugin(octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(
			css=["css/cyborgorange.css",
			"css/bootstrap-modal.css",
			"css/overrides.css",
			"css/overrides-icons.css"],
			 js=["js/octoprint-cyborgorangetheme.js"]
	)

	
	def get_update_information(self):
		return dict(
			cyborgtheme=dict(
				displayName="Cyborg Orange Theme",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-CyborgOrangeTheme",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/Octoprint-CyborgOrangeTheme/archive/{target_version}.zip"
		)
	)

__plugin_name__ = "Cyborg Orange Theme"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = __plugin_implementation__ = CyborgOrangeThemePlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}