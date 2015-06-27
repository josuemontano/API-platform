angular.module('demo', ['demo.controllers', 'demo.services', 'ui.router', 'satellizer', 'restangular', 'angular-loading-bar'])
    .config(['RestangularProvider', '$authProvider', '$stateProvider', '$urlRouterProvider', function(RestangularProvider, $authProvider, $stateProvider, $urlRouterProvider) {
        RestangularProvider.setBaseUrl('/api/v1');

        $authProvider.facebook({
            clientId: '0000000000000',
        });
        $authProvider.google({
            clientId: '388525728293-bu96shbpa47dpc92efgsemsd6ftu7gj7.apps.googleusercontent.com',
        });
        $authProvider.loginRedirect = '/dashboard/posts';
        $authProvider.loginUrl = '/login';

        $stateProvider
        .state('home', {
            url:'/',
            templateUrl: 'static/ui/home.html',
            controller: 'HomeCtrl',
            controllerAs: 'vm',
        })
        // Login & logout
        .state('login', {
            url:'/login',
            templateUrl: 'static/ui/login.html',
            controller: 'LoginCtrl',
            controllerAs: 'vm',
        })
        .state('logout', {
            url:'/logout',
            template: null,
            controller: 'LogoutCtrl'
        })
        // Dashboard (private)
        .state('dashboard', {
            url:'/dashboard',
            abstract: true,
            templateUrl: 'static/ui/dashboard/index.html',
            data: {
                authenticate: true,
            },
        })
        .state('dashboard.posts', {
            url:'/posts',
            templateUrl: 'static/ui/dashboard/posts.html',
            controller: 'PostsCtrl',
            controllerAs: 'vm',
            resolve: {
                posts: ['Posts', function (Posts) {
                    return Posts.getList();
                }]
            },
        });
        $urlRouterProvider.otherwise('/');
    }])
    .run(['$rootScope', '$state', '$auth', function ($rootScope, $state, $auth) {
        $rootScope.$on('$stateChangeStart', function(event, toState) {
            if (toState.data && toState.data.authenticate && !$auth.isAuthenticated()) {
                $state.transitionTo('login');
                event.preventDefault();
            }
        })
    }]);