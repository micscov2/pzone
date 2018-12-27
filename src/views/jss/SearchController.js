// Angular Js lessons
// ng-bind binds $scope -> view
// ng-model is two way binding $scope <--> view

myApp.controller('SearchController', ['$scope', '$http', function($scope, $http) {
    // Initialize undefined variables
    $scope.textData = "";
    $scope.records = [];
    $scope.totalRecords = 0;
    $scope.selectedBookMarks = [];

    var successResponseHandler = function(response) {
        $scope.records = [];
        for (var i = 0; i < response.data.length; i++) {
            lineData = response.data[i]['line'];
            lineData = lineData.replace(/DOUBLE_QUOTE/g, '"')
                               .replace(/SINGLE_QUOTE/g, "'")
            $scope.records.push(lineData);
        }
        $scope.totalRecords = $scope.records.length;
    };

    var successResponseHandlerBookmarks = function(response) {
        console.log(response);
        $scope.selectedBookMarks = [];
    };

    var errorResponseHandler = function(errorResponse) {
        console.log(errorResponse);
    };

    $scope.searchClicked = function() {
        subject = $scope.subject;
        userInput = $scope.textData;
        $http.get("http://127.0.0.1:7880/pzone/v1/search/" 
                    + subject 
                    + "?term=" 
                    + userInput)
                    .then(successResponseHandler, errorResponseHandler);
    };

    $scope.saveBookMark = function(record) {
        $scope.selectedBookMarks.push(record);
    };

    $scope.saveSelectedBookmarks = function() {
        data = $scope.selectedBookMarks;
        $http.post("http://pzone:7880/catalogue/addBookmarks", data)
            .then(successResponseHandlerBookmarks, errorResponseHandler);
    }
}]);
