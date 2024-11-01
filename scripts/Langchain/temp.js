
$(document).ready(function () {
    $('#searchButton').on('click', function () {
        var comCntstSpclt = $("#cntstSpcltSelect").val();
        var screeningStatus = $("#screeningStatus").val();
        $.ajax({
            url: '/cnst/selectSrngProc.do',
            cache: false,
            type: "GET",
            contentType: "application/x-www-form-urlencoded; charset=UTF-8",
            data: {
                //TODO : seqComCntstSpclt로 파라미터화
                seqComCntstSpclt: 101,
                noEpsdSrng: 1,
                screeningStatus: screeningStatus
            },
            beforeSend: function (xhr) {
                xhr.setRequestHeader(header, token);
            },
            success: function (response) {
                console.log("AJAX success called : selectSrngProc" + screeningStatus);
                $('#proc_table').html(response); // Or use .replaceWith(result) if appropriate
            },
            error: function (request, status, error) {
                console.log("code: " + request.status);
                console.log("message: " + request.responseText);
                console.log("error: " + error);
            }
        });
    });
});

$(document).ready(function () {
    $(document).on('click', 'button[name="evaluateButton"]', function () {
        var seq = $(this).data('seq');
        var seqSpcltCntst = $(this).data('seqspcltcntst');
        console.log("Evaluate button clicked. seq:", seq);
        console.log("Evaluate button clicked. seqSpcltCntst:", seqSpcltCntst);
        loadEvaluationTable(seq, seqSpcltCntst);
        document.querySelector('.table_wrap.evaluate').scrollIntoView({
            behavior: 'smooth'
        });
    });
});
