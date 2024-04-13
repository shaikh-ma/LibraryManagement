  function filter_books(){
    selection = document.getElementsByTagName("select");
    console.log(selection)
    avl_books = document.querySelectorAll(".card");
    for (let i=0; i < avl_books.length; i++){
      txt = avl_books[i].children[4].innerText;
      if (selection[0].value == 'By availability' && txt == "Status: True"){
        avl_books[i].style.display = 'none';
      }
      else {
        avl_books[i].style.display = 'inline-flex';
      }
    }
  }
