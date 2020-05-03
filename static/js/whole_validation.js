$(function()
{
  //バリデーション
  $('.alert').hide();
 

  $("#submitBtn").click(function(){

    // 各値を入れるオブジェクト
    var sendFlag = true;
     
    // テキストの値を取得
    $(".whole_thema_txt_box #text").each(function(){
        if(this.value == ""){
            sendFlag = sendFlag && false
        }
    });
    
    if(sendFlag == false){
      $(".whole_thema_txt_box .alert").show();
      return false;
    }else{
      $(".whole_thema_txt_box .alert").hide();
    }
    
  });
});