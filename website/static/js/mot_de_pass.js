$(document).ready(function(){
    $('.pass_show').append('<span class="ptxt">Show</span>');  
    $('.pass_show input').attr('type', 'password'); // Cache le texte par défaut
});

$(document).on('click', '.pass_show span.ptxt', function(){ 
    $(this).text($(this).text() == "Show" ? "Hide" : "Show"); 
    var type = $(this).text() == "Show" ? 'password' : 'text';
    $(this).prev().attr('type', type); 
});
