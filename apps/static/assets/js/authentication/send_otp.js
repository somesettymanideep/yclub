
function sendOTP(){
    const mobile = $("#phone_number").val()
    if (!validateMobile(mobile)) {
        show_error('Invalid mobile number');
        return;
    }
    let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
      url: '/send_otp/',
      method: 'POST',
      data: {'mobile': mobile,'csrfmiddlewaretoken': csrfmiddlewaretoken},
      success: function(response){
        userId = response['user_id']
        window.location.href = "/otp_validate/";
      },
      error: function(response){
        show_error(response.responseJSON['error'])
      }
    })
  }

  function validateMobile(mobile) {
    const mobilePattern = /^[0-9]{10}$/;
    return mobilePattern.test(mobile);
}
