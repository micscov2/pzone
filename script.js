//var myApp = angular.module('myApp');

// Angular Js lessons
// ng-bind binds $scope -> view
// ng-model is two way binding $scope <--> view

myApp.controller('MainController', ['$scope', '$http', function($scope, $http) {
    // Initialize undefined variables
    $scope.textData = "";
    $scope.pzk = "pzk";
    var successResponseHandler = function (response) {
        $scope.resultRecv1 = response.data.split(":->:")[0]
        $scope.resultRecv2 = response.data.split(":->:")[1]
        // Check why x, y = a.split("") doesn't work
    };
    var errorResponseHandler = function(errorResponse) {
        console.log(errorResponse);
    };

    $scope.searchClicked = function (){
        userInput = $scope.textData;
        $http.get("http://pzone:7880/catalogue/search/" + userInput)
             .then(successResponseHandler, errorResponseHandler);
    }
}]);


myApp.controller('Other1Controller', ['$scope', function($scope) {
    $scope.pzk1 = "pzk1_other1";
}]);
