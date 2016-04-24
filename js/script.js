jQuery(document).ready(function(){
    $('#timeInfo').timepicker({ 'scrollDefault': 'now', 'step': 5 });
    
    $("#flight-submit").on("submit", function(event){
        var time = $('#timeInfo').val();
        var flight = $('#flightNum').val();
        console.log('clicked')

        $.ajax("www.shotamakino.com", {'flight': flight, 'time': time}, function(data){
            /*use data here
            
            */
        })
        event.preventDefault();
    })
    
});

