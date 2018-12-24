var myApp = angular.module('myApp', ["ngRoute"]);

myApp.config(function($routeProvider) {
    $routeProvider
        .when("/search", {
            templateUrl: "search.html",
            controller: "SearchController"
        })
        .when("/createNew", {
            templateUrl: "createNew.html",
            controller: "CreateNewController"
        })
        .when("/bookmarks", {
            templateUrl: "bookmarks.html",
            controller: "BookmarksController"
        })
        .when("/topHits", {
            templateUrl: "topHits.html",
            controller: "TopHitsController"
        });
    // .otherwise({redirectTo: "/main"});
});
