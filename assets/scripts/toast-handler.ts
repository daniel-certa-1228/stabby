'use strict';

import { bootstrap } from './index';

document.addEventListener('DOMContentLoaded', function() {
    const toasts: NodeListOf<Element> = document.querySelectorAll('.message-toast');
    
    toasts.forEach(function(toast: Element) {
        const bootstrapToast: bootstrap.Toast = new bootstrap.Toast(toast);
        
        bootstrapToast.show();
    });
  });
  