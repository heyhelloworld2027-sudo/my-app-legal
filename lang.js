(function(){
  var SUP=['ar','en','ru','ur','es','de','fr','tr','zh','hi'],RTL=['ar','ur'];
  var saved=null;try{saved=localStorage.getItem('lang')}catch(e){}
  var nav=(navigator.language||'en').toLowerCase().slice(0,2);
  var l=SUP.indexOf(saved)>-1?saved:(SUP.indexOf(nav)>-1?nav:'en');
  function set(x){
    document.documentElement.setAttribute('data-lang',x);
    document.documentElement.lang=x;
    document.documentElement.dir=RTL.indexOf(x)>-1?'rtl':'ltr';
    try{localStorage.setItem('lang',x)}catch(e){}
    var s=document.getElementById('langSel');if(s)s.value=x;
  }
  set(l);
  document.addEventListener('DOMContentLoaded',function(){
    var s=document.getElementById('langSel');
    if(s)s.addEventListener('change',function(){set(s.value)});
    set(l);
  });
})();
