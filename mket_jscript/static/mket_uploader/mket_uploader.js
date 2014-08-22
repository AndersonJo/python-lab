/**
 * Mket File Uploader Module
 */
MketFileUploader = function(data) {
	/**
	 * @param target : target div element
	 * @param only : it's like a filter. (images, image, videos, video)
	 * 
	 * this.videoUploader = new MketFileUploader({
			'target' : this.videoFileContainerEl,
			'policyData' : this.videoPolicyData,
			'only' : ['video']
		});
		
		
		File Input Element가 보이는데..
		displya;hidden 으로는 안되고.. 화면 밖으로 내보내야 한다.
		
		.file_container_input{
			position: absolute;
			left: -1000px;
			top: -1000px;
			margin-top: 3px;
			margin-bottom: 3px;
		}
	 */
	this.mketItems = [];

	// Required Arguments
	this.targetEl = data['target'];
	this.only = data['only']; 

	// HTML Arguments
	this.url = this.targetEl.attr('data-url');
	this.name = this.targetEl.attr('data-name');
	this.text = this.targetEl.attr('data-text');
	this.className = this.targetEl.attr('data-class');
	this.multiple = this.targetEl.attr('data-multiple');

	if (!this.url) {
		this.url = data['url'];
	}
	if (!this.name) {
		this.name = data['name'];
	}
	if (!this.className) {
		this.className = data['className'];
	}
	if (!this.text) {
		this.text = data['text'];
	}
	if (!this.multiple) {
		this.multiple = data['multiple'];
	}	
	if(!this.only ){
		this.only = [];
	}

	if (this.multiple != null) {
		this.multiple = this.multiple.toLowerCase() == 'true' || this.multiple == 'multiple' ? true : false;
	}
	
	// Set the class attribute to Target Element
	this.targetEl.addClass(this.className);

	// Create a Form Element
	this.formEl = $('<form></form>');
	this.formEl.attr('method', "post");
	this.formEl.attr('action', this.url);
	this.formEl.attr('enctype', "multipart/form-data");
	this.formEl.attr('onsubmit', 'return false;');
	this.formEl.attr('class', this.className + "_form");

	// Create a Button Element
	this.buttonEl = $('<button></button>');

	// Create a File Input Element
	this.uploadEl = $('<input></input>');

	// Create a File List Container Element
	this.containerEl = $('<div></div>');
	this.containerEl.attr('class', this.className + "_container");
	this.containerEl.hide();


	// Append the Elements
	this.formEl.append(this.buttonEl);
	this.formEl.append(this.uploadEl);
	this.formEl.append(this.containerEl);
	this.targetEl.append(this.formEl);

	// Initialization
	this._initOnly();
	this._notifyInputClicked();
	this._initListeners(); 
	this.clearFileListContainer();
};

MketFileUploader.prototype._initOnly = function() {
	if(!this.only){
		this.only = [];
	}
	
	var only = [];
	for(var i=0; i<this.only.length; i++){
		var key = this.only[i];
		if(key == "image" || key == "images"){
			only.push('image/jpeg');
			only.push('image/jpg');
			only.push('image/png');
			only.push('image/gif');
		}
		
		if(key == "video" || key == "videos"){
			only.push('video/mp4');
			only.push('video/asf');
			only.push('video/video/x-ms-asf');			
			only.push('video/avi');
			only.push('video/msvideo');
			only.push('video/x-msvideo');
			only.push('video/mpeg');
			only.push('video/x-mpeg');
			only.push('video/quicktime');
		}
	}
	this.only = only;
};

MketFileUploader.prototype._notifyInputClicked = function() {
	var self = this;
	// Create a Button Element
	var buttonEl = $('<button></button>');
	buttonEl.attr('type', 'button');
	buttonEl.attr('class', this.className + '_button');
	buttonEl.text(this.text);

	// Create a File Input Element
	var uploadEl = $('<input></input>');
	uploadEl.attr('type', 'file');
	uploadEl.attr('name', this.name);
	uploadEl.attr('class', this.className + "_input");
	if (this.multiple) {
		uploadEl.attr('multiple', 'multiple');
	}

	this.buttonEl.replaceWith(buttonEl);
	this.uploadEl.replaceWith(uploadEl);

	this.buttonEl = buttonEl;
	this.uploadEl = uploadEl;

	// listen Upload Button
	this.buttonEl.on('click', function(e) {
		if(!self._hasSent){
			self.uploadEl.trigger('click', function(e) {
				console.log(e);
			});
		}
	});

	// listen File Input
	this.uploadEl.on('change', function(e) {
		self.updateList(this.files, e);
		self._notifyInputClicked();
	});
};
MketFileUploader.prototype._initListeners = function(name, size) {
	var self = this;

};

MketFileUploader.prototype.notifyFileDestroyed = function(name, size) {

	// Remove the seletected item.
	var itemLength = this.mketItems.length;
	for (var i = 0; i < itemLength; i++) {
		var item = this.mketItems[i];
		if (item.name == name && item.size == size) {
			this.mketItems.splice(this.mketItems.indexOf(item), 1);
			break;
		}
	};

	// Restructure files
	var files = [];
	for (var i = 0; i < itemLength; i++) {
		var item = this.mketItems[i];
		files.push(item);
	}

	// Recreate all files.
	this.mketItems = [];
	this.clearFileListContainer();
	this.updateList(files, null);

	itemLength = this.mketItems.length;
	if (itemLength <= 0) {
		this.containerEl.fadeOut();
	}
};

MketFileUploader.prototype.clearFileListContainer = function(files, e) {
	var self = this;
	if (!this.multiple) {
		this.mketItems = [];
	}

	this.containerEl.empty();
};

MketFileUploader.prototype.getUploadedFileNames = function(files, e) {
	var response = [];
	var items = this.mketItems.slice(0);
	for(var i=0; i< items.length; i++){
		var fileItem = items[i];
		var name = fileItem.getUploadedFileName();
		response.push(name);
	}
	return response;
};

MketFileUploader.prototype.getFiles = function(files, e) {
	var response = [];
	for(var i=0; i< this.mketItems.length; i++){
		var fileItem = this.mketItems[i];
		var file = fileItem.getFile();
		response.push(file);
	};
	return response;
};



MketFileUploader.prototype.updateList = function(files, e) {
	this.clearFileListContainer();

	var fileClassName = this.className + "_list_item";
	var filesLength = files.length;
	for (var i = 0; i < filesLength; i++) {
		var file = files[i];
		var args = {};
		
		if (file) {
			if(this.only.length == 0 || $.inArray(file.type, this.only) != -1){
				
				// Check Duplicate File Name
				var isValidFile = true;
				for(var j=0; j<this.mketItems.length; j++){
					if(this.mketItems[j].name == file.name){
						isValidFile = false;
						break;
					}
				}
				
				if(isValidFile){
					args['file'] = file;
					args['class'] = fileClassName;
					var item = new MketFileUploaderItem(this, args);
					this.mketItems.push(item);
				}
			}
			else{
				this.handleOnlyError();
			}
		}
	}

	var itemLength = this.mketItems.length;
	for (var i = 0; i < itemLength; i++) {
		var mketItem = this.mketItems[i];
		var itemEl = mketItem.getElement();
		this.containerEl.append(itemEl);
	}

	if (itemLength > 0) {
		this.containerEl.show();
	}
};

MketFileUploader.prototype.send = function() {
	this._hasSent = true;
	this.buttonEl.fadeOut();
	
	for (var i = 0; i < this.mketItems.length; i++) {
		var formData = new FormData();
		var uploadingItems = this.mketItems.slice(0);
		var uploadingItem = uploadingItems[i];
		// Clone

		// Initialize AWS POST Form Data
		for (var j = 0; j < this.policyFormData.length; j++) {
			var formDataItem = this.policyFormData[j];
			var dataKey = formDataItem[0];
			var dataValue = formDataItem[1];

			if (dataKey == "key") {
				dataValue += "-"+ i.toString();
				uploadingItem.setUploadedFileName(dataValue);
			}

			if (dataKey == "Content-Type") {
				dataValue += uploadingItem.type;
			}

			formData.append(dataKey, dataValue);
		}

		//formData.append('Content-Type', this.mketItems[i].type);
		formData.append('file', uploadingItem.getFile());
		this._send(uploadingItems[i], formData);
	}
};

MketFileUploader.prototype._send = function(mketItem, formData) {
	var self = this;
	
	// remove Delete Button of File Item
	mketItem.removeDeleteButton();
	
	$.ajax({
		url : this.url, //Server script to process data
		type : 'POST',
		xhr : function() {// Custom XMLHttpRequest
			var xhr = $.ajaxSettings.xhr();
			if (xhr.upload) {// Check if upload property exists
				xhr.upload.addEventListener('progress', function(e) {
					if (e.lengthComputable) {
						var percentComplete = e.loaded / e.total;
						self.handleProgress(e.loaded, e.total, mketItem);
					}
				}, false);
				// For handling the progress of the upload
			}
			return xhr;
		},
		//Ajax events
		//beforeSend : this.handleBeforeSend,
		success : this.handleComplete,
		error : this.handleError,
		// Form data
		data : formData,
		cache : false,
		contentType : false,
		processData : false,
		crossDomain: true,
		//Options to tell jQuery not to process data or worry about content-type.
	});
};


MketFileUploader.prototype.handleOnlyError = function() {
	//console.log('MketFileUploader handleProgress', loaded, total, mketItem);
	if(noty){
		noty({
			'layout' : 'bottom',
			'type' : 'error',
			'timeout' : 1000,
			'text' : '형식에 맞지 않는 파일입니다'
		});
	}
};

MketFileUploader.prototype.handleProgress = function(loaded, total, mketItem) {
	//console.log('MketFileUploader handleProgress', loaded, total, mketItem);
	mketItem.notifyProgress(loaded, total);
};

MketFileUploader.prototype.handleBeforeSend = function(e) {
	console.log('MketFileUploader handleProgress', e);
};

MketFileUploader.prototype.handleError = function(xhr, textStatus, error) {
	console.log('MketFileUploader handleError xhr', xhr);
	console.log('MketFileUploader handleError textStatus', textStatus);
	console.log('MketFileUploader handleError error', error);
};

MketFileUploader.prototype.handleComplete = function(data, textStatus, xhr) {
	console.log('MketFileUploader handleComplete data:', data);
	console.log('MketFileUploader handleComplete textStatus:', textStatus);
	console.log('MketFileUploader handleComplete xhr:', xhr);
};

/**
 * **************************************************************************
 * Mket File Uploader List Item
 * **************************************************************************
 */

MketFileUploaderItem = function(mketFileUploader, data) {
	this._context = mketFileUploader;
	this.file = data['file'];
	this.className = data['class'];
	this.name = this.file.name;
	this.size = this.file.size;
	this.type = this.file.type;

	this.initHtml();
	this.initListeners();
};

MketFileUploaderItem.prototype.initHtml = function() {
	this.containerEl = $('<div>\
	<div style="display: table; width:100%;">\
		<div style="display: table-row;">\
		<div id="a" style="display: table-cell; vertical-align: top;"></div>\
		<div id="b" style="display: table-cell; vertical-align: top;"></div>\
		<div id="c" style="display: table-cell; vertical-align: top; width:100%; text-align:right;"></div>\
	</div>\</div></div>');
	this.containerEl.attr('class', this.className);

	var aEl = $('#a', this.containerEl);
	var bEl = $('#b', this.containerEl);
	var cEl = $('#c', this.containerEl);

	this.nameEl = $('<span></span>');
	this.nameEl.attr('class', this.className + "_name");
	this.nameEl.text(this.name);

	this.sizeEl = $('<span></span>');
	this.sizeEl.attr('class', this.className + "_size");
	this.sizeEl.text(" (" + this.size.toString() + "kb)");

	this.deleteEl = $('<div></div>');
	this.deleteEl.attr('class', this.className + "_delete");

	this.progressContainerEl = $('<div></div>');
	this.progressContainerEl.attr('class', this.className + "_progress_container");
	this.progressContainerEl.hide();

	this.progressBarEl = $('<div></div>');
	this.progressBarEl.attr('class', this.className + "_progress_bar");
	
	aEl.append(this.nameEl);
	bEl.append(this.sizeEl);
	cEl.append(this.deleteEl);
	
	this.progressContainerEl.append(this.progressBarEl);
	this.containerEl.append(this.progressContainerEl);
	

	aEl.removeAttr('id');
	bEl.removeAttr('id');
	cEl.removeAttr('id');
};

MketFileUploaderItem.prototype.initListeners = function() {
	var self = this;
	this.deleteEl.on('click', function(e) {
		self.destroy();
	});
};

MketFileUploaderItem.prototype.getFile = function() {
	return this.file;
};

MketFileUploaderItem.prototype.getUploadedFileName = function() {
	return this._uploadedFileName;
};

MketFileUploaderItem.prototype.destroy = function() {
	//this.containerEl.remove();
	console.log('MketFileUploaderItem destroy:', this.name, this.size);
	this._context.notifyFileDestroyed(this.name, this.size);

};

MketFileUploaderItem.prototype.getElement = function() {
	return this.containerEl;
};

MketFileUploaderItem.prototype.removeDeleteButton = function(loaded, total) {
	this.deleteEl.hide();	
};

MketFileUploaderItem.prototype.setUploadedFileName = function(uploadedFileName) {
	this._uploadedFileName = uploadedFileName;
};

MketFileUploaderItem.prototype.notifyProgress = function(loaded, total) {
	this.progressContainerEl.show();
	console.log('MketFileUploaderItem', loaded, total);
	
	var totalWidth = this.progressContainerEl.width();
	var floatingPencentage = loaded / total;
	this.progressBarEl.width(totalWidth * floatingPencentage);
	
	this.sizeEl.text( " "+ (Math.round(floatingPencentage*100)).toString() +"% " );
	
};
