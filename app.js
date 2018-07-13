var myApp = angular.module('myApp', ["ngRoute"]);

myApp.config(function($routeProvider) {
    $routeProvider
        .when("/main", {
            templateUrl: "index.html",
            controller: "MainController"
        })
        .when("/other1", {
            templateUrl: "other1.html",
            controller: "Other1Controller"
        })
        .otherwise({redirectTo: "/main"});
});

