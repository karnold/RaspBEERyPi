(function($) {
    $(document).ready(function() {
        printReading();

        setInterval(function() {
            printReading();
        }, 1000);
    });

    function printReading() {
        $.ajax({
            url: 'current-reading',
            dataType: 'json',
            success: function(data) {
                $('.latest-readings').html('Currently ' + data.f + ' F');
            }   
        }); 
    }

})(jQuery);
