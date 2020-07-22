 $("#pesquisa_form").submit(function (e) {
        // preventing from page reload and default actions
        e.preventDefault();
        // serialize the data for sending the form data.
        var serializedData = $(this).serialize();
        // make POST ajax call
        $.ajax({
            type: 'POST',
            url: "{% url 'pesquisa' %}",
            data: serializedData,
            success: function (response) {
                // on successfull creating object
                // 1. clear the form.
                $("#pesquisa_form).trigger('reset');
                // 2. focus to nickname input
                $("#pesquisa").focus();
            },
            error: function (response) {
                // alert the error if any error occured
                alert(response["responseJSON"]["error"]);
            }
        })
    })