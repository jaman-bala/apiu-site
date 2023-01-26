HTMLElement.prototype.InitSlider = function (options = null) {
    var sliderIndex = 2;
    this.style.height = "750px";
    var model = [
      { zIndex: 0, left: "30%" },
      { zIndex: 1, left: "40%" },
      { zIndex: 2, left: "50%" },
      { zIndex: 1, left: "60%" },
      { zIndex: 0, left: "70%" }
    ];
    const setPosition = (tempModel, img, index) => {
      img.style.zIndex = tempModel[index].zIndex;
      img.style.transform = `translateX(-50%) scale(${
        0.6 + tempModel[index].zIndex * 0.2
      })`;
      img.style.left = tempModel[index].left;
      tempModel[index].zIndex != 2
        ? (img.style.filter = options?.filter ?? "blur(1px)")
        : (img.style.filter = null);
    };
    const gotoNext = () => {
      if (++sliderIndex == 5) sliderIndex = 0;
      this.children[sliderIndex].click();
    };
    const gotoBack = () => {
      if (--sliderIndex == -1) sliderIndex = 4;
      this.children[sliderIndex].click();
    };
  
    var count = this.childElementCount;
    for (let index = 0; index < count; index++) {
      var image = this.children[index];
      setPosition(model, image, index);
      image.style.width = "1000px";
      image.style.border = "1px solid gray";
      image.style.padding = "6px";
      image.style.borderRadius = "8px";
      image.style.position = "absolute";
      image.style.transition = "1s";
      image.onclick = function () {
        sliderIndex = index;
        const arrNew = [...model];
        var shifts = index + 3;
        if (shifts > 4) shifts -= 5;
  
        for (let i = 0; i < shifts; i++) arrNew.unshift(arrNew.pop());
  
        for (let findex = 0; findex < count; findex++)
          setPosition(arrNew, this.parentNode.children[findex], findex);
      };
    }
    setInterval(() => {
      if (options?.timerEnable ?? true)
        options?.slider?.toLowerCase()?.trim() == "gotoback"
          ? gotoBack()
          : gotoNext();
    }, options?.timerInterval ?? 5000);
  };
  
  document.getElementById("Slider").InitSlider({
    timerInterval: 3000,
    timerEnable: true,
    filter: "grayscale(1)",
    slider: "gotoBack"
  });