myApp.controller('CreateNewController', ['$scope', '$http', function($scope, $http) {

    $scope.items = [];

    $scope.addNewitem = function() {
        var newItemNo = $scope.items.length + 1;
        $scope.items.push({ 'id': newItemNo, 'name': 'item' + newItemNo });
    };

    $scope.removeNewitem = function(item) {
        var indx = -1;
        for (var i = 0; i < $scope.items.length; i++) {
        	if (item.name === $scope.items[i].name) {
        		indx = i;
        		break;
        	}
        }

        if (indx != -1) {
        	$scope.items.splice(indx, 1);
        	console.log(indx);
        }
    };

    // $scope.showAdditem = function(item) {
    //     return item.id === $scope.items[$scope.items.length - 1].id;
    // };

    var successResponseHandler = function(response) {
        console.log("Success, probably");
    };

    var errorResponseHandler = function(errorResponse) {
        console.log("Failure");
    };

    $scope.saveToFile = function() {
    	// document.getElementById("2").value
    	var data = {"filename": "SYSTEM_TAKEN"}
    	for (var i = 1; i <= $scope.items.length; i++) {
    		value = document.getElementById(i).value;
    		data[i] = value;
    	}
    	console.log(data);

    	// post(url, data, [config]);
    	$http.post("http://pzone:7880/catalogue/addNew", data)
            .then(successResponseHandler, errorResponseHandler);
    };
}]);