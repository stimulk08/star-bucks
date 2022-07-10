for (var p of document.getElementsByClassName('menu-button')) {
  p.onclick = function() {
    for (var button of document.getElementsByClassName('menu-button')) {
        button.color = 'white'
    }
     this.style.color = '#FF8C00';
  }
}