function loadchat(){
  ajaxGetRequest('/chat',renderchat)
}


function renderchat(response){
  let newline='<br>';
  let chat='';
  let chatdiv=document.getElementById('chat');
  let messagelist=JSON.parse(response);
  for (let data of messagelist){
    chat=chat + data['message'] + newline;
  }
  chatdiv['innerHTML']=chat;
}


function sendmessage(){
  let messagetext=document.getElementById('message');
  let message=messagetext['value'];
  messagetext['value']='';
  let tosend=JSON.stringify({'message':message})
  ajaxPostRequest('/send', tosend, renderchat)
}







