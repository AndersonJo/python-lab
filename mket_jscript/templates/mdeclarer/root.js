declare = {};
declare = function(name) {
	var names = name.split('.');
	var size = names.length;
	for (var i = 0; i < size; i++) {
		var text = "";
		for (var j = 0; j <= i; j++) {
			text += names[j];

			if (i != j) {
				text += '.';
			}
		};

		if (eval('typeof ' + text + ' == "undefined"')) {
			eval(text + ' =  {}');
		}
	};
};

var alertFallback = false;
   if (typeof console === "undefined" || typeof console.log === "undefined") {
     console = {};
     if (alertFallback) {
         console.log = function(msg) {
              alert(msg);
         };
     } else {
         console.log = function() {};
     }
   }