// let loadMoreBtn = document.querySelector("#load-more");
// let currentItem = 3;

// loadMoreBtn.onclick = () => {
//   let boxes = [
//     ...document.querySelectorAll(".container__news .box-container .box"),
//   ];
//   for (var i = currentItem; i < currentItem + 3; i++) {
//     boxes[i].style.display = "inline-block";
//   }
//   currentItem += 3;

//   if (currentItem >= boxes.length) {
//     loadMoreBtn.style.display = "none";
//   }
// };


var swiper = new Swiper(".slide-content", {
  slidesPerView: 3,
  spaceBetween: 25,
  loop: true,
  centerSlide: 'true',
  fade: 'true',
  grabCursor: 'true',
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
  breakpoints: {
    0: {
      slidesPerView: 1,
    },
    520: {
      slidesPerView: 2,
    },
    950: {
      slidesPerView: 3,
    },
  }
});

