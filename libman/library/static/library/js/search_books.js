function findBook() {
search_for = $('#searchbook').val().toLowerCase();
titles = $('.card-title');
bookcards = $('.card');

for (let i=0; i<titles.length; i++){
  title = titles[i].innerText.toLowerCase();
  match = title.indexOf(search_for);
  if (match > -1){
    bookcards[i].style.display = "block"
  }
  else{
        bookcards[i].style.display = "none"
  }
  }
}