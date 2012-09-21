(function($) {
    $(document).ready(function() {
        printReading();

        setInterval(function() {
            printReading();
        }, 300);
    });

    function printReading() {
        $.ajax({
            url: 'current-reading',
            dataType: 'json',
            success: function(data) {
                var temp = $('select.temp-type').val();
                if (temp == 'f') {
                    tempReading = data.f + ' F';
                } else {
                    tempReading = data.c + ' C';
                }
                $('.latest-readings .temp').html(tempReading);
                $('.latest-readings .gravity').html(data.gravity);
            }   
        }); 
    }

})(jQuery);
