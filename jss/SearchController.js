//var myApp = angular.module('myApp');

// Angular Js lessons
// ng-bind binds $scope -> view
// ng-model is two way binding $scope <--> view

myApp.controller('SearchController', ['$scope', '$http', function($scope, $http) {
    // Initialize undefined variables
    $scope.textData = "";
    $scope.records = [];
    var successResponseHandler = function(response) {
        // $scope.records = [response.data.split(":->:")];
        $scope.records = [];
        for (var property in response.data) {
            if (!response.data.hasOwnProperty(property)) {
                continue;
            }

            filename = response.data[property];
            $scope.records.push(filename + " -> " + property);
        }
        // $scope.resultRecv2 = response.data.split(":->:")[1]
        // Check why x, y = a.split("") doesn't work
    };
    var errorResponseHandler = function(errorResponse) {
        console.log(errorResponse);
    };

    $scope.searchClicked = function() {
        userInput = $scope.textData;
        $http.get("http://pzone:7880/catalogue/search/" + userInput)
            .then(successResponseHandler, errorResponseHandler);
    }
}]);