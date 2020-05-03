$(function()
{
  //バリデーション
  $('.alert').hide();

  $("#submitBtn").click(function(){

    var sendFlag = true;

    if(!$(".main_thema_txt_box #text").val()){
      $(".main_thema_txt_box .alert").show();
      sendFlag = false;
    }else{
      $(".main_thema_txt_box .alert").hide();
    }

    if(sendFlag == false){
      return false;
    }    
  });
});