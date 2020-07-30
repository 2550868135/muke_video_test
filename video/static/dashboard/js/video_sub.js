$(function () {
    var inputNumber = $('#number');
    var inputUrl = $('#url');
    var videosubInputId = $('#videosub-input-id');
    $('.update-btn').click(function () {
        var vediosubId = $(this).attr('data_id');
        var videoSubNumber = parseInt($(this).attr('data-number'));
        var vedioSubUrl = $(this).attr('data-url');
        
        inputNumber.val(videoSubNumber);
        inputUrl.val(vedioSubUrl);
        videosubInputId.val(vediosubId);
            })
  });