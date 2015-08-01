/* UI
__________________________________________________________________________ */

// TODO: Improve this code when more tabs are needed
var tabUI = {
	currentTab: 'content',
	showMode: 'mobile',
	windowWidth: window.innerWidth,

	contentSection: undefined,
	infoSection: undefined,

	leftTab: undefined,
	rightTab: undefined,

	initTabs: function(contentSectionId, infoSectionId, leftTabId, rightTabId) {
		this.setSections(contentSectionId, infoSectionId);
		this.setTabs(leftTabId, rightTabId);

		this.setClickEvents();
		this.setResizeWindowEvent();
	},

	setSections: function(contentSectionId, infoSectionId) {
		this.contentSection = document.getElementById(contentSectionId);
		this.infoSection = document.getElementById(infoSectionId);
	},

	setTabs: function(leftTabId, rightTabId) {
		this.leftTab = document.getElementById(leftTabId);
		this.rightTab = document.getElementById(rightTabId);
	},

	setClickEvents: function() {
		var that = this;
		this.leftTab.addEventListener('click', function() {
			that.currentTab = 'content';
			that.setSectionsVisibility();
		});

		var that = this;
		this.rightTab.addEventListener('click', function() {
			that.currentTab = 'info';
			that.setSectionsVisibility();
		});
	},

	setResizeWindowEvent: function() {
		var that = this;
		window.addEventListener('resize', function(event){
			that.windowWidth = window.innerWidth;
			that.setShowMode();
		});
	},

	setShowMode: function() {
		if (this.windowWidth < 900) { this.showMode = 'mobile'; }
		else { this.showMode = 'desktop'; }

		this.setSectionsVisibility();
	},

	setSectionsVisibility: function() {
		if ( this.showMode == 'mobile' ) {
			if ( this.currentTab == 'content' ) {
				this.leftTab.classList.add('tab_selected');
				this.rightTab.classList.remove('tab_selected');

				this.contentSection.style.display = 'block';
				this.infoSection.style.display = 'none';
			}
			else if ( this.currentTab == 'info' ) {
				this.leftTab.classList.remove('tab_selected');
				this.rightTab.classList.add('tab_selected');

				this.contentSection.style.display = 'none';
				this.infoSection.style.display = 'block';
			}
		}
		else if ( this.showMode == 'desktop' ) {
			this.contentSection.style.display = 'block';
			this.infoSection.style.display = 'block';
		}
	},
}


/* functionality
__________________________________________________________________________ */

var infiniteScrolling = {
	pageNumber: 2,
	scroll: true,
	listUrl: '',

	init: function(listUrl) {
		this.listUrl = listUrl;

		// TODO: add to the total height the header and the tab
		if ($('#content').height() < $(window).height()) {
			this.ajaxCall();
		}

		var that = this;
		$(window).scroll(function() {
			if (this.scroll) {
				// TODO: change to if currentTab is content
				//if ( currentTab == 'content') {
					if($(window).scrollTop() + $(window).height() == $(document).height()) {
						that.ajaxCall();
					}
				//}
			}
		});
	},

	ajaxCall: function() {
		$.ajax({
			type: 'GET',
			url: this.listUrl,
			data: { 'page' : this.pageNumber, },
			dataType: 'html',
			success: this.pageSuccess.bind(this),
			error: this.pageError.bind(this),
		});
	},

	pageError: function() {
		this.scroll = false;
		$('#loading').hide();
	},

	pageSuccess: function(data) {
		this.pageNumber = this.pageNumber + 1;
		$(data).insertAfter($('.entry_card').last());
	},
}
