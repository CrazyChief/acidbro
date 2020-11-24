(function ($) {
  'use strict';
  $(document).ready(() => {
    toggleRelatedUseButtonControls();

    $(document).on('change', '#id_use_button', () => {
      toggleRelatedUseButtonControls();
    });
  });
})(django.jQuery);

toggleRelatedUseButtonControls = () => {
  const useButton = $('#id_use_button');
  const relatedUseButtonControls = useButton.parents('.form-row').nextAll();

  relatedUseButtonControls.each((i, e) => {
    if (i <= 1 && useButton[0].checked) {
      $(e).show();
    } else if (i > 1) {
      console.log();
    } else {
      $(e).hide();
    }
  });
};
