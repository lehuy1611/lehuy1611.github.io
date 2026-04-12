/* ==========================================================================
   Theme Toggle — dark / light mode with localStorage persistence.
   Loads before the page renders (placed in <head>) to prevent flash.
   ========================================================================== */

(function () {
    'use strict';

    var STORAGE_KEY = 'theme';

    function getPreferred() {
        var saved = localStorage.getItem(STORAGE_KEY);
        if (saved === 'dark' || saved === 'light') return saved;
        // Fall back to OS preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return 'dark';
        }
        return 'light';
    }

    function apply(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem(STORAGE_KEY, theme);
    }

    // Apply immediately (script is in <head>) to prevent flash of wrong theme
    apply(getPreferred());

    // Once DOM is ready, wire up the toggle button(s)
    document.addEventListener('DOMContentLoaded', function () {
        var buttons = document.querySelectorAll('.theme-toggle');
        buttons.forEach(function (btn) {
            btn.addEventListener('click', function () {
                var current = document.documentElement.getAttribute('data-theme') || 'light';
                apply(current === 'dark' ? 'light' : 'dark');
            });
        });
    });
})();
