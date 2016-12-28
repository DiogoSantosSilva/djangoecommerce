/**
 * Created by diogo on 27/11/16.
 */

  function showMessageFlash(message) {
            //var template = "{% include 'alert.html'  with message='" + message +"'%}"
            var template = "<div class='container container-alert-flash'>" +
                "<div class='col-sm-offset-8 col-sm-4'>" +
                "<div class=' alert alert-success alert-dismissable' role='alert'>" +
                "<button class='close' data-dismiss='alert' aria-label='Close'>" +
                "<span aria-hidden='true'>&times;</span></button>"
                + message + "</p></div></div></div>"
            $("body").append(template);
            $(".container-alert-flash").fadeIn();
            setTimeout(function (){
                $(".container-alert-flash").fadeOut();
            },1000)
  }