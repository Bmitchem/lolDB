/**
 * Created by bob on 15/04/15.
 */
$(document).ready(function(){
     $('#search_input_box').keyup(function(){
        var query;
        query = $( this ).val();
        $.get('/armory/champion_search/', {suggestion: query}, function(data){
            var $target = $('#side_bar_search_div');
            $target.html(data);
            $('#search_row').show();
        });
    });
});
