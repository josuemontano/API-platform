(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{181:function(e,t,n){"use strict";n(182),n(384);var o=n(108);n(386),n(388);var u=void 0;!function(){var e=n(391).default;u=(0,o.render)((0,o.h)(e,null),document.body,u)}()},388:function(e,t,n){},391:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=c(n(158)),u=c(n(164)),a=c(n(165)),i=c(n(166)),l=c(n(175)),r=n(108),s=c(n(431));function c(e){return e&&e.__esModule?e:{default:e}}var d=function(e){function t(){return(0,u.default)(this,t),(0,i.default)(this,(t.__proto__||(0,o.default)(t)).apply(this,arguments))}return(0,l.default)(t,e),(0,a.default)(t,[{key:"render",value:function(){return(0,r.h)("div",{class:"starter-template"},(0,r.h)("div",{class:"container"},(0,r.h)("div",{"uk-grid":!0},(0,r.h)("div",{class:"uk-width-1-4"}),(0,r.h)("div",{class:"uk-width-1-2"},(0,r.h)("div",{class:"content"},(0,r.h)("h1",null,(0,r.h)("span",{class:"font-semi-bold"},"Pyramid")," ",(0,r.h)("span",{class:"smaller"},"Alchemy project")),(0,r.h)("p",{class:"lead"},"Welcome to ",(0,r.h)("span",{class:"font-normal"},"canopus"),", a Pyramid application generated by",(0,r.h)("br",null),(0,r.h)("span",{class:"font-normal"},"Cookiecutter"),"."),(0,r.h)(s.default,{googleClientID:window.googleClientID,windowsClientID:window.windowsClientID}))))))}}]),t}(r.Component);t.default=d},431:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=d(n(158)),u=d(n(164)),a=d(n(165)),i=d(n(166)),l=d(n(175)),r=d(n(432)),s=n(433),c=n(108);function d(e){return e&&e.__esModule?e:{default:e}}var f=function(e){function t(e){(0,u.default)(this,t);var n=(0,i.default)(this,(t.__proto__||(0,o.default)(t)).call(this,e));return r.default.init({google:e.googleClientID,windows:e.windowsClientID},{display:"page",page_uri:window.location.href,redirect_uri:"/login"}),n.loginUserOnRedirect(),n}return(0,l.default)(t,e),(0,a.default)(t,[{key:"loginUserOnRedirect",value:function(){var e=(0,r.default)("google").getAuthResponse();e||(e=(0,r.default)("windows").getAuthResponse()),e&&(0,s.authenticate)(e)}},{key:"render",value:function(){return(0,c.h)("p",{"uk-margin":!0},(0,c.h)("button",{type:"button",onClick:t.onGoogleLogin,class:"uk-button uk-button-primary"},"Entrar con Google"),(0,c.h)("button",{type:"button",onClick:t.onWindowsLogin,class:"uk-button uk-button-secondary"},"Entrar con Microsoft"))}}],[{key:"onGoogleLogin",value:function(){(0,r.default)("google").login({scope:"openid, email",force:!0})}},{key:"onWindowsLogin",value:function(){(0,r.default)("windows").login({scope:"email",force:!0})}}]),t}(c.Component);t.default=f},433:function(e,t,n){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var o=a(n(434));t.getUserCredentials=function(){return JSON.parse(localStorage.getItem("user"))||{}},t.onLogin=i,t.authenticate=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{};u.default.post("/auth/"+e.network,{access_token:e.access_token}).then(function(e){return e.data}).then(function(e){return i(e.user,e.access_token)}).catch(function(e){alert("User could not login")})};var u=a(n(436));function a(e){return e&&e.__esModule?e:{default:e}}function i(e,t){!function(e,t){var n={id:e.id,access_token:t};localStorage.setItem("user",(0,o.default)(n))}(e,t),window.location="/"}}},[[181,2,1]]]);
//# sourceMappingURL=app.a0dc29ae.js.map