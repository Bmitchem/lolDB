/**
 * Created by bob on 15/04/15.
 */
$(document).ready(function(){
     $('#search_input_box').keyup(function(){
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
    $('.champion_page_link').click(function(){
        var champ_id = $( this).data('champion-id');
        var $target = $('#page-wrapper');
        $.get('/armory/champion/', {champ_id: champ_id}, function(data){
            $target.html(data);
        });
    });
});
