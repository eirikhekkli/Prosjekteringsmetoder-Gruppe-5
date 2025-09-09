// HavShipping – felles skript (tema-mekanikk)
(function(){
  const KEY = 'havshipping-theme';
  const el  = document.documentElement;
  const btn = document.getElementById('themeToggle');

  // init fra lagret preferanse
  const stored = localStorage.getItem(KEY);
  if (stored) {
    if (stored === 'light') el.setAttribute('data-theme','light');
    else el.removeAttribute('data-theme');
    btn && btn.setAttribute('aria-pressed', stored === 'light');
  }

  function setTheme(next){
    if(next === 'light') el.setAttribute('data-theme','light');
    else el.removeAttribute('data-theme');
    localStorage.setItem(KEY, next);
    btn && btn.setAttribute('aria-pressed', next === 'light');
  }

  btn && btn.addEventListener('click', ()=>{
    const next = el.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
    setTheme(next);
  });
})();
