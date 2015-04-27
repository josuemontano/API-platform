angular.module('demo', ['demo.controllers', 'demo.services', 'demo.directives', 'ui.router', 'ngResource'])
    .config(['$resourceProvider', '$stateProvider', '$urlRouterProvider', function($resourceProvider, $stateProvider, $urlRouterProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;

        $stateProvider
        .state('home', {
            url:'/',
            templateUrl: 'static/ui/home.html',
            controller: 'HomeCtrl'
        })
        .state('login', {
            url:'/login',
            templateUrl: 'static/ui/login.html',
            controller: 'LoginCtrl'
        })
        .state('dashboard', {
            url:'/dashboard',
            templateUrl: 'static/ui/dashboard/index.html',
            controller: 'DashboardCtrl'
        });
        $urlRouterProvider.otherwise('/');
    }]);