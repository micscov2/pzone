var myApp = angular.module('myApp', ["ngRoute"]);

myApp.config(function($routeProvider) {
    $routeProvider
        .when("/search", {
            templateUrl: "views/search.html",
            controller: "SearchController"
        })
        .when("/createNew", {
            templateUrl: "views/createNew.html",
            controller: "CreateNewController"
        })
        .when("/bookmarks", {
            templateUrl: "views/bookmarks.html",
            controller: "BookmarksController"
        })
        .when("/topHits", {
            templateUrl: "views/topHits.html",
            controller: "TopHitsController"
        });
    // .otherwise({redirectTo: "/main"});
});