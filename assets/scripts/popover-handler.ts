'use strict';

import { bootstrap } from './index';

// SERVER-RENDERED POPOVERS
document.addEventListener('DOMContentLoaded', function() {
  const popoverTriggerList: NodeListOf<Element> = document.querySelectorAll('[data-bs-toggle="popover"]');
  
    // eslint-disable-next-line no-unused-vars
  const popoverList: bootstrap.Popover[] = Array.from(popoverTriggerList).map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));
});

//GRID POPOVERS
const initGridPopovers = (): void => {
  const popovers: HTMLCollectionOf<Element> = document.getElementsByClassName('grid-popover');

  const popoverList: bootstrap.Popover[] = Array.from(popovers).map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));
}

export {
  initGridPopovers
}
