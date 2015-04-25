/**
 * Created by bob on 15/04/15.
 */
$(document).ready(function(){
    $('#search_input_box_champions').keyup(function () {
        //var champions = ["Annie","Olaf","Galio","Twisted Fate","Xin Zhao","Urgot","LeBlanc","Vladimir","Fiddlesticks","Kayle","Master Yi","Alistar","Ryze","Sion","Sivir","Soraka","Teemo","Tristana","Warwick","Nunu","Miss Fortune","Ashe","Tryndamere","Jax","Morgana","Zilean","Singed","Evelynn","Twitch","Karthus","Cho'Gath","Amumu","Rammus","Anivia","Shaco","Dr. Mundo","Sona","Kassadin","Irelia","Janna","Gangplank","Corki","Karma","Taric","Veigar","Trundle","Swain","Caitlyn","Blitzcrank","Malphite","Katarina","Nocturne","Maokai","Renekton","Jarvan IV","Elise","Orianna","Wukong","Brand","Lee Sin","Vayne","Rumble","Cassiopeia","Skarner","Heimerdinger","Nasus","Nidalee","Udyr","Poppy","Gragas","Pantheon","Ezreal","Mordekaiser","Yorick","Akali","Kennen","Garen","Leona","Malzahar","Talon","Riven","Kog'Maw","Shen","Lux","Xerath","Shyvana","Ahri","Graves","Fizz","Volibear","Rengar","Varus","Nautilus","Viktor","Sejuani","Fiora","Ziggs","Lulu","Draven","Hecarim","Kha'Zix","Darius","Jayce","Lissandra","Diana","Quinn","Syndra","Zyra","Gnar","Zac","Yasuo","Vel'Koz","Braum","Jinx","Lucian","Zed","Vi","Aatrox","Nami","Azir","Thresh","Rek'Sai","Kalista","Bard"];
        var query;
        query = $( this ).val();
        $.get('/armory/champion_search/', {suggestion: query}, function(data){
            if(query){
                var $target = $('#side_bar_search_div');
                $target.html(data);
                $('#search_row').show();
            }else{
                $('#search_row').hide();
            }
        });

    });
    $('#search_input_button_players').click(function () {
        var query;
        query = $('#search_input_box_players').val();
        $.get('/armory/player_search/', {suggestion: query}, function (data) {
            var $target = $('#page-wrapper');
            $target.html(data);
        });

    });
    $('.champion_page_link').click(function(){
        var champ_id = $( this).data('champion-id');
        var $target = $('#page-wrapper');
        $.get('/armory/champion/', {champ_id: champ_id}, function(data){
            $target.html(data);
        });
    });
});
