/**
 * Created by bob on 01/05/15.
 */

(function(){
    var app = angular.module('matchHistory', []);

    app.controller('MatchController', ['$http', function ($http) {
        var matchHistory = this;
        matchHistory.matchInfo = {};
        $http.get('https://na.api.pvp.net/api/lol/na/v2.2/match/1790213909?includeTimeline=True&api_key=8e9b4f1f-29ff-45cc-b49d-dc5f20636f03').success(function(data){
            matchHistory.matchInfo = data;
        });

    }]);
});

