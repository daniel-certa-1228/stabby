'use strict';

import { bootstrap } from './index';

document.addEventListener('DOMContentLoaded', function() {
  const popoverTriggerList: NodeListOf<Element> = document.querySelectorAll('[data-bs-toggle="popover"]');
  
    // eslint-disable-next-line no-unused-vars
  const popoverList = Array.from(popoverTriggerList).map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));
});
