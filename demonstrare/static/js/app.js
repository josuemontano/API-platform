angular.module('demo', ['demo.controllers', 'demo.services', 'demo.directives', 'ui.router', 'satellizer', 'ngResource'])
    .config(['$resourceProvider', '$authProvider', '$stateProvider', '$urlRouterProvider', function($resourceProvider, $authProvider, $stateProvider, $urlRouterProvider) {
        $resourceProvider.defaults.stripTrailingSlashes = false;

        $authProvider.facebook({
            clientId: '0000000000000',
            redirectUri: window.location.origin + '/auth/facebook',
        });
        $authProvider.google({
            clientId: '1073147924054-vfo1c5atj8j84u2170smt863554m36br.apps.googleusercontent.com',
            redirectUri: window.location.origin + '/auth/google',
        });
        $authProvider.loginRedirect = '/dashboard';
        $authProvider.loginUrl = '/login';

        $stateProvider
        .state('home', {
            url:'/',
            templateUrl: 'static/ui/home.html',
            controller: 'HomeCtrl'
        })
        // Login & logout
        .state('login', {
            url:'/login',
            templateUrl: 'static/ui/login.html',
            controller: 'LoginCtrl'
        })
        .state('logout', {
            url:'/logout',
            template: null,
            controller: 'LogoutCtrl'
        })
        // Dashboard (private)
        .state('dashboard', {
            url:'/dashboard',
            templateUrl: 'static/ui/dashboard/index.html',
            controller: 'DashboardCtrl',
            authenticate: true
        });
        $urlRouterProvider.otherwise('/');
    }])
    .run(['$rootScope', '$state', '$auth', function ($rootScope, $state, $auth) {
        $rootScope.$on('$stateChangeStart', function(event, toState, toParams, fromState, fromParams) {
            if (toState.authenticate && !$auth.isAuthenticated()) {
                $state.transitionTo('login');
                event.preventDefault();
            }
        })
    }]);