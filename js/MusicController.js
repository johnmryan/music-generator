var app = angular.module('musicApp',[]);
app.controller('MusicController', ['$scope', function($scope) {
	var vm = this;
	vm.notes = undefined;
	
	vm.generate = function() {
		if (vm.notes) {
			console.log("vm.notes is defined");
		}
	}

}]);
