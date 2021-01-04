(function ($) {
  $(document).ready(() => {
    const formSets = $('#slideritem_set-group, #review_set-group');
    formSets.fadeOut(500);

    const sliderType = $('#id_type_slider');
    const selectedOption = sliderType.find('option:selected');

    if (+selectedOption.val() === 0) {
      $('#slideritem_set-group').fadeIn(500);
    } else if (+selectedOption.val() === 1) {
      $('#review_set-group').fadeIn(500);
    } else {
      formSets.fadeOut();
    }

    $(document).on('change', '#id_type_slider', (el) => {
      const target = $(el.currentTarget);
      target.find('option').filter((i, e) => {
        if (e.selected && e.value === '0') {
          $('#slideritem_set-group').fadeIn(500);
          $('#review_set-group').fadeOut(500);
        } else if (e.selected && e.value === '1') {
          $('#review_set-group').fadeIn(500);
          $('#slideritem_set-group').fadeOut(500);
        } else if (e.selected && e.value === '') {
          formSets.fadeOut();
        }
      });
    });
  });
})(django.jQuery);
