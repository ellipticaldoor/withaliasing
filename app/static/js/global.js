/* UI
__________________________________________________________________________ */

// Tab manager -- TODO: Improve this code when more tabs are needed

var tabUI = {
	currentTab: 'content',
	showMode: 'mobile',
	windowWidth: window.innerWidth,

	contentSection: undefined,
	infoSection: undefined,

	leftTab: undefined,
	rightTab: undefined,

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

	initTabs: function(contentSectionId, infoSectionId, leftTabId, rightTabId) {
		this.setSections(contentSectionId, infoSectionId);
		this.setTabs(leftTabId, rightTabId);

		this.setClickEvents();
		this.setResizeWindowEvent();
	},
}


/* functionality
__________________________________________________________________________ */

// infinite scrolling
