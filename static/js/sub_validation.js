$(function()
{
  //バリデーション
  $('.alert').hide();
 

  $("#submitBtn").click(function(){

    // 各値を入れるオブジェクト
    var sendFlag = true;
     
    // テキストの値を取得
    $(".sub_thema_txt_box #text").each(function(){
        if(this.value == ""){
            sendFlag = sendFlag && false
        }
    });
    
    if(sendFlag == false){
      $(".sub_thema_txt_box .alert").show();
      return false;
    }else{
      $(".sub_thema_txt_box .alert").hide();
    }
    
  });
});