'use strict';

import { bootstrap } from './index';

document.addEventListener('DOMContentLoaded', function() {
    const toasts = document.querySelectorAll('.toast');
    toasts.forEach(function(toast) {
        const bootstrapToast = new bootstrap.Toast(toast);
        bootstrapToast.show();
    });
  });