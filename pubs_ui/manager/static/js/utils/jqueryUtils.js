/* jslint browser: true */
/* global define */

define([
	'jquery'
], function($) {
	"use strict";

	var utils = (function() {
		var self = {};

		self.createDivInContainer = function($container) {
			var $newDiv = $('<div />');
			$container.append($newDiv);

			return $newDiv;
		};

		return self;
	})();

	return utils;
});
