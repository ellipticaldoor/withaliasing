/* UI
__________________________________________________________________________ */

// Tab manager -- TODO: Improve this code when more tabs are needed

var tabUI = {
	currentTab: 'content',

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
		this.leftTab.addEventListener('click', function() {
			tabUI.leftTab.classList.add('tab_selected');
			tabUI.rightTab.classList.remove('tab_selected');

			tabUI.contentSection.style.display = 'block';
			tabUI.infoSection.style.display = 'none';
		});

		this.rightTab.addEventListener('click', function() {
			tabUI.leftTab.classList.remove('tab_selected');
			tabUI.rightTab.classList.add('tab_selected');

			tabUI.contentSection.style.display = 'none';
			tabUI.infoSection.style.display = 'block';
		});
	},

	initTabs: function(contentSectionId, infoSectionId, leftTabId, rightTabId) {
		this.setSections(contentSectionId, infoSectionId);
		this.setTabs(leftTabId, rightTabId);

		this.setClickEvents();
	},
}


/* functionality
__________________________________________________________________________ */

// infinite scrolling
