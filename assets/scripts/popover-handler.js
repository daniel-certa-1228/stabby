'use strict';

import { bootstrap } from './index';

document.addEventListener('DOMContentLoaded', function() {
  const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');

  // eslint-disable-next-line no-unused-vars
  const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));
});
