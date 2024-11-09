function register_user() {
    const phoneNumber = $('#phonenumber').val();
    const email = $('#useremail').val();
    const pan = $('#pan').val();
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        url: '/user_register/',
        type: 'POST',
        data: {
            'phone_number': phoneNumber,
            'email': email,
            'pan': pan,
            'csrfmiddlewaretoken': csrfToken
        },
        success: function (response) {
            window.location = response['path']
        },
        error: function (response) {
            show_error(response.responseJSON['error'])
        }
    });
}