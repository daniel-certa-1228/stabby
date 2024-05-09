'use strict';

document.addEventListener("click", function(e){
    const knifeDetailTarget = e.target.closest(".knife-detail-btn");
    const sharpenerDetailTarget = e.target.closest(".sharpener-detail-btn");
    const bladeEditTarget = e.target.closest(".blade-edit-btn");
    const bladeDeleteTarget = e.target.closest(".blade-delete-btn");
    const knifeWorkLogEditTarget = e.target.closest(".knife-wl-edit-btn");
    const knifeWorkLogDeleteTarget = e.target.closest(".knife-wl-delete-btn");
    const sharpenerWorkLogEditTarget = e.target.closest(".sharpener-wl-edit-btn");
    const sharpenerWorkLogDeleteTarget = e.target.closest(".sharpener-wl-delete-btn");


    if (knifeDetailTarget) {

      console.log('knifeDetailTarget', knifeDetailTarget.value);

    } else if (sharpenerDetailTarget) {

        console.log('sharpenerDetailTarget', sharpenerDetailTarget.value);

    } else if (bladeEditTarget) {

        console.log('bladeEditTarget', bladeEditTarget.value);

    } else if (bladeDeleteTarget) {

        console.log('bladeDeleteTarget', bladeDeleteTarget.value);

    }  else if (knifeWorkLogEditTarget) {

        console.log('knifeWorkLogEditTarget', knifeWorkLogEditTarget.value);

    } else if (knifeWorkLogDeleteTarget) {

        console.log('knifeWorkLogDeleteTarget', knifeWorkLogDeleteTarget.value);

    } else if (sharpenerWorkLogEditTarget) {

        console.log('sharpenerWorkLogEditTarget', sharpenerWorkLogEditTarget.value);
        
    } else if (sharpenerWorkLogDeleteTarget) {

        console.log('sharpenerWorkLogDeleteTarget', sharpenerWorkLogDeleteTarget.value);

    } else {
        console.log('No Target');
    }
  });