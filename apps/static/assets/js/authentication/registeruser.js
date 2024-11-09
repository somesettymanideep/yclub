// function register_user() {
//     const phoneNumber = $('#phonenumber').val();
//     const email = $('#useremail').val();
//     const pan = $('#pan').val();
//     const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

//     $.ajax({
//         url: '/user_register/',
//         type: 'POST',
//         data: {
//             'phone_number': phoneNumber,
//             'email': email,
//             'pan': pan,
//             'csrfmiddlewaretoken': csrfToken
//         },
//         success: function (response) {
//             window.location = response['path']
//         },
//         error: function (response) {
//             show_error(response.responseJSON['error'])
//         }
//     });
// }

function register_user() {
    const username = $('#validationTooltipUsername').val();
    const phoneNumber = $('#phonenumber').val();
    const email = $('#useremail').val();
    const city = $('#validationCustom03').val();
    const state = $('#validationCustom04').val();
    const zip = $('#validationCustom05').val();
    const password = $('#example-password-input').val();
    const csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        url: '/user_register/',
        type: 'POST',
        data: {
            'username': username,
            'phone_number': phoneNumber,
            'email': email,
            'city': city,
            'state': state,
            'zip': zip,
            'password': password,
            'csrfmiddlewaretoken': csrfToken
        },
        success: function (response) {
            window.location = response['/'];
        },
        error: function (response) {
            show_error(response.responseJSON['error']);
        }
    });
}
