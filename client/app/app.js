'use strict';

angular.module('demo', [
    // Auth
    'demo.auth.controller',
    // Home
    'demo.home.controller',
    // Posts
    'demo.post.controller',
    'demo.post.service',

    'demo.controllers',
    // 3rd party
    'ui.router',
    'satellizer',
    'restangular',
    'angular-loading-bar'
])
.config(['RestangularProvider', '$authProvider', '$stateProvider', '$urlRouterProvider', function (RestangularProvider, $authProvider, $stateProvider, $urlRouterProvider) {
    RestangularProvider.setBaseUrl('/api/v1');
    RestangularProvider.setResponseExtractor(function (response, operation) {
        if (operation === 'getList') {
            var data = response;
            if (_.has(response, 'meta')) {
                data = response.data;
                data.meta = response.meta;
            }
            return data;
        }
        return response;
    });

    $authProvider.facebook({
        clientId: '448167108683079',
    });
    $authProvider.google({
        clientId: '388525728293-bu96shbpa47dpc92efgsemsd6ftu7gj7.apps.googleusercontent.com',
    });
    $authProvider.loginRedirect = '/dashboard/posts';
    $authProvider.loginUrl = '/login';

    $stateProvider
    .state('home', {
        url:'/',
        templateUrl: 'static/ui/home/home.html',
        controller: 'HomeCtrl',
        controllerAs: 'vm',
    })
    // Login & logout
    .state('login', {
        url:'/login',
        templateUrl: 'static/ui/auth/login.html',
        controller: 'LoginCtrl',
        controllerAs: 'vm',
    })
    .state('logout', {
        url:'/logout',
        template: null,
        controller: 'LogoutCtrl',
        data: {
            authenticate: true,
        },
    })
    // Dashboard (private)
    .state('dashboard', {
        url:'/dashboard',
        abstract: true,
        template: '<div ui-view></div>',
        data: {
            authenticate: true,
        },
    })
    .state('dashboard.posts', {
        url:'/posts',
        templateUrl: 'static/ui/post/posts.html',
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
    $rootScope.$on('$stateChangeStart', function (event, toState) {
        if (toState.data && toState.data.authenticate && !$auth.isAuthenticated()) {
            $state.transitionTo('login');
            event.preventDefault();
        }
    })
}]);
