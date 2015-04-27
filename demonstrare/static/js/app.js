angular.module('demo', ['demo.controllers', 'demo.directives', 'ui.router'])
    .config(['$stateProvider', '$urlRouterProvider', function($stateProvider, $urlRouterProvider) {
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
        });
        $urlRouterProvider.otherwise('/');
    }]);