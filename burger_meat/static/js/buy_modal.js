$(document).ready(function() {
    $('.minus').click(function () {
        var $input = $(this).parent().find('.input_count');
        var count = parseInt($input.val()) - 1;
        count = count < 1 ? 1 : count;
        $input.val(count);
        $input.change();
        return false;
    });
     $('.plus').click(function () {
        var $input = $(this).parent().find('.input_count');
        $input.val(parseInt($input.val()) + 1);
     $input.change();
        return false;
    });
});

