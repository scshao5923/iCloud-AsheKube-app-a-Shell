
function stkQry(){
    $(".salTy").each(function(){
        if ($(this).text()=='賣'){
	    $(this).css("background-color","orange");
	    $(this).siblings().css("background-color","orange");
	}else{
	    $(this).css("background-color","white");
	    $(this).siblings().css("background-color","white");
	}
    });
}

const app = Vue.createApp({
	data() {
	 return {
	  message: "交易明細表"
	 }
	}
   })
   
   app.mount('#app')
 