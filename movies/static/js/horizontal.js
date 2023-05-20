let currentScrollPosition = 0;
let scrollAmount = 200;

const sCont = document.querySelector(".menu-container");
const hScroll = document.querySelector(".horizontal-scroll");
const btnScrollLeft = document.querySelector("#btn-scroll-left");
const btnScrollRight = document.querySelector("#btn-scroll-right");


// const cCont = document.querySelectorAll(".menu-circle").length;


btnScrollLeft.style.opacity= "0";

// let max = cCont;
let maxScroll= -sCont.offsetWidth + hScroll.offsetWidth;

function scrollHorizonatally(val){
    let maxScroll= -sCont.offsetWidth + hScroll.offsetWidth;
    currentScrollPosition += (val * scrollAmount);

    if(currentScrollPosition > 0){
        currentScrollPosition= 0;
        btnScrollLeft.style.opacity="0";
    }else{
        btnScrollLeft.style.opacity="1";
    }


    if(currentScrollPosition < maxScroll){
        currentScrollPosition = maxScroll;
        btnScrollRight.style.opacity="0";
    }else{
        btnScrollRight.style.opacity="1";
    }
    sCont.style.left = currentScrollPosition + "px";

}