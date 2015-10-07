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
    $rootScope.$on('$stateChangeStart', function (event, toState) {
        if (toState.data && toState.data.authenticate && !$auth.isAuthenticated()) {
            $state.transitionTo('login');
            event.preventDefault();
        }
    })
}]);

angular.module('demo.auth.controller', ['satellizer'])
    .controller('LoginCtrl', ['$auth', LoginCtrl])
    .controller('LogoutCtrl', ['$auth', LogoutCtrl]);

/**
 * @name LoginCtrl
 * @type {Function}
 */
function LoginCtrl ($auth) {
    var vm = this;
    vm.authenticate = function (provider) {
        $auth.authenticate(provider)
        .then(function (response) {
        }, function (error) {
            if (error.status === 400)
                vm.error = 'You cannot login to this site. Request an account.';
            else
                vm.error = 'An unexpected problem occured, please try again.';
        });
    };
}

/**
 * @name LogoutCtrl
 * @type {Function}
 */
function LogoutCtrl ($auth) {
    $auth.logout();
}

angular.module('demo.home.controller', [])
    .controller('HomeCtrl', [HomeCtrl]);

/**
 * @name HomeCtrl
 * @type {Function}
 */
function HomeCtrl () {
    var vm = this;
    vm.message = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.';
}

angular.module('demo.post.controller', ['demo.post.service'])
    .controller('PostsCtrl', ['posts', PostsCtrl]);

/**
 * @name PostsCtrl
 * @type {Function}
 */
function PostsCtrl (posts) {
    var vm = this;
    vm.posts = posts;
}

angular.module('demo.post.service', ['restangular'])
    .factory('Posts', ['Restangular', PostsFactory]);

/**
 * @name PostsFactory
 * @type {Function}
 */
function PostsFactory (Restangular) {
    return Restangular.service('posts');
}

angular.module('demo.controllers', ['satellizer'])
    .controller('MenuCtrl', ['$scope', '$auth', MenuCtrl]);

/**
 * @name MenuCtrl
 * @type {Function}
 */
function MenuCtrl ($scope, $auth) {
    $scope.isAuthenticated = function () {
        return $auth.isAuthenticated();
    };
}
