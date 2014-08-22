mtools = {};

mtools.validateEmail = function(email) {
	var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	return regex.test(email);
};

mtools.place = function(pivotEl, overEl) {
	// .position() uses position relative to the offset parent,
	var pos = pivotEl.position();

	// .outerWidth() takes into account border and padding.
	var width = pivotEl.outerWidth();

	//show the menu directly over the placeholder
	overEl.css({
		position : "absolute",
		top : pos.top + "px",
		left : (pos.left + width) + "px"
	}).show();
};

mtools.getCookie = function(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) == (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
};

mtools.getDjangoCSRF = function() {
	return mtools.getCookie('csrftoken');
};
mtools.getCsrf = mtools.getDjangoCSRF;

mtools.csrfSetup = function() {

	$.ajaxSetup({
		'beforeSend' : function(xhr) {
			xhr.setRequestHeader('X-CSRFToken', mtools.getCookie('csrftoken'));
		}
	});
};

/**
 * Image Check Box Module
 */
mtools.ImageCheckBox = function(data) {
	var self = this;
	this.rootEl = data['rootEl'] || $('<button type="button"></button>');
	this.check = data['check'];
	this.checkedImgUrl = data['checkedImgUrl'];
	this.uncheckedImgUrl = data['uncheckedImgUrl'];
	this.message = this.rootEl.text().trim() || data['message'];
	this.className = data['class'];

	this.check = this.check == "true" || this.check == "checked" || this.check == true ? true : false;
	this.rootEl.data({
		'check' : this.check
	});

	// init Root Element
	this.rootEl.empty();
	this.rootEl.addClass(this.className);

	// create a new image element
	this.imgEl = $('<img>');
	this.imgEl.addClass(this.className + "_image");
	this.imgEl.attr('src', this.check ? this.checkedImgUrl : this.uncheckedImgUrl);
	this.rootEl.append(this.imgEl);

	this.textEl = $('<span>');
	this.textEl.addClass(this.className + "_text");
	this.textEl.text(this.message);
	this.rootEl.append(this.textEl);

	this.rootEl.on('click', function(e) {
		var value = self.rootEl.data()['check'];

		if (value) {
			self.imgEl.attr('src', self.uncheckedImgUrl);
			self.textEl.text(self.message);
			self.rootEl.data({
				'check' : false
			});
			self.check = false;
		} else {
			self.imgEl.attr('src', self.checkedImgUrl);
			self.textEl.text(self.message);
			self.rootEl.data({
				'check' : true
			});
			self.check = true;
		}
		self.onClick(self.check);
	});

	this.rootEl.on('mouseover', function(e) {
		self.imgEl.addClass(self.className + "_image_hover");
		self.textEl.addClass(self.className + "_text_hover");
	});

	this.rootEl.on('mouseout', function(e) {
		self.imgEl.removeClass(self.className + "_image_hover");
		self.textEl.removeClass(self.className + "_text_hover");
	});
};

mtools.ImageCheckBox.prototype.getElement = function() {
	return this.rootEl;
};

mtools.ImageCheckBox.prototype.getValue = function() {
	return this.check;
};

mtools.ImageCheckBox.prototype.onClick = function(check) {
	console.log("please override this method");
};

$.base64 = ( function($) {
		var _PADCHAR = "=", _ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/", _VERSION = "1.0";

		function _getbyte64(s, i) {
			// This is oddly fast, except on Chrome/V8.
			// Minimal or no improvement in performance by using a
			// object with properties mapping chars to value (eg. 'A': 0)

			var idx = _ALPHA.indexOf(s.charAt(i));

			if (idx === -1) {
				throw "Cannot decode base64";
			}

			return idx;
		}

		function _decode(s) {
			var pads = 0, i, b10, imax = s.length, x = [];

			s = String(s);

			if (imax === 0) {
				return s;
			}

			if (imax % 4 !== 0) {
				throw "Cannot decode base64";
			}

			if (s.charAt(imax - 1) === _PADCHAR) {
				pads = 1;

				if (s.charAt(imax - 2) === _PADCHAR) {
					pads = 2;
				}

				// either way, we want to ignore this last block
				imax -= 4;
			}

			for ( i = 0; i < imax; i += 4) {
				b10 = (_getbyte64(s, i) << 18 ) | (_getbyte64(s, i + 1) << 12 ) | (_getbyte64(s, i + 2) << 6 ) | _getbyte64(s, i + 3);
				x.push(String.fromCharCode(b10 >> 16, (b10 >> 8 ) & 0xff, b10 & 0xff));
			}

			switch ( pads ) {
				case 1:
					b10 = (_getbyte64(s, i) << 18 ) | (_getbyte64(s, i + 1) << 12 ) | (_getbyte64(s, i + 2) << 6 );
					x.push(String.fromCharCode(b10 >> 16, (b10 >> 8 ) & 0xff));
					break;

				case 2:
					b10 = (_getbyte64(s, i) << 18) | (_getbyte64(s, i + 1) << 12 );
					x.push(String.fromCharCode(b10 >> 16));
					break;
			}

			return x.join("");
		}

		function _getbyte(s, i) {
			var x = s.charCodeAt(i);

			if (x > 255) {
				throw "INVALID_CHARACTER_ERR: DOM Exception 5";
			}

			return x;
		}

		function _encode(s) {
			if (arguments.length !== 1) {
				throw "SyntaxError: exactly one argument required";
			}

			s = String(s);

			var i, b10, x = [], imax = s.length - s.length % 3;

			if (s.length === 0) {
				return s;
			}

			for ( i = 0; i < imax; i += 3) {
				b10 = (_getbyte(s, i) << 16 ) | (_getbyte(s, i + 1) << 8 ) | _getbyte(s, i + 2);
				x.push(_ALPHA.charAt(b10 >> 18));
				x.push(_ALPHA.charAt((b10 >> 12 ) & 0x3F));
				x.push(_ALPHA.charAt((b10 >> 6 ) & 0x3f));
				x.push(_ALPHA.charAt(b10 & 0x3f));
			}

			switch ( s.length - imax ) {
				case 1:
					b10 = _getbyte(s, i) << 16;
					x.push(_ALPHA.charAt(b10 >> 18) + _ALPHA.charAt((b10 >> 12 ) & 0x3F) + _PADCHAR + _PADCHAR);
					break;

				case 2:
					b10 = (_getbyte(s, i) << 16 ) | (_getbyte(s, i + 1) << 8 );
					x.push(_ALPHA.charAt(b10 >> 18) + _ALPHA.charAt((b10 >> 12 ) & 0x3F) + _ALPHA.charAt((b10 >> 6 ) & 0x3f) + _PADCHAR);
					break;
			}

			return x.join("");
		}

		return {
			decode : _decode,
			encode : _encode,
			VERSION : _VERSION
		};

	}(jQuery) );

mtools.getQueryString = function() {
	var response = {}, hash, k;
	var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
	for (var i = 0; i < hashes.length; i++) {
		hash = hashes[i].split('=');
		response[hash[0]] = decodeURIComponent(hash[1]);
	}
	return response;
};

mtools.digits = function(text){
	return text.toString().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,");
}

$.fn.digits = function() {
	return this.each(function() {
		$(this).text($(this).text().replace(/(\d)(?=(\d\d\d)+(?!\d))/g, "$1,"));
	});
};

$.fn.exists = function(){return this.length>0;}