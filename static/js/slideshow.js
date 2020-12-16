var myIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("mySlides");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  myIndex++;
  if (myIndex > x.length) {myIndex = 1}
  x[myIndex-1].style.display = "block";
  setTimeout(carousel, 4000); // Change image every 2 seconds
}


setInterval(function(){
    var $container = $('.js-slideshow'),
        $currentImage = $container.find('.mySlides'),
        currentImageIndex = $currentImage.index() + 1,
        imagesLength = $container.find('img').length;

    $currentImage.removeClass('mySlides');
    $currentImage.next('img').addClass('mySlides');

    if ( currentImageIndex == imagesLength ) {
        $container.find('img').first().addClass('mySlides');
    }
}, 5000)
