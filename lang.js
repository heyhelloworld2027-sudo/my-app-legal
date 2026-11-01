(function(){
  var saved=null;try{saved=localStorage.getItem('lang')}catch(e){}
  var l=saved||((navigator.language||'en').toLowerCase().indexOf('ar')===0?'ar':'en');
  function set(x){
    document.documentElement.setAttribute('data-lang',x);
    document.documentElement.lang=x;
    document.documentElement.dir=x==='ar'?'rtl':'ltr';
    try{localStorage.setItem('lang',x)}catch(e){}
    document.querySelectorAll('.lang button').forEach(function(b){b.classList.toggle('on',b.dataset.set===x)});
  }
  document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('.lang button').forEach(function(b){b.addEventListener('click',function(){set(b.dataset.set)})});
    set(l);
  });
  set(l);
})();