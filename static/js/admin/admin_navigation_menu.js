(function ($) {
  'use strict';
  $(document).ready(() => {
    toggleFooter();

    $(document).on('change', '#id_menu_type', () => {
      toggleFooter();
    });

    $(document).on('click', '#navigationlinks_set-group .add-row a', () => {
      toggleFooter();
    });

    $(document).on('change', '[id$="-link_to"]', (e) => {
      const target = $(e.currentTarget);
      const options = target.find('option');
      options.each((i, e) => {
        if ($(e).css('display') !== 'none') {
          if ($(e).val() === "0" && e.selected) {
            target.parents('fieldset').find('.field-link').show();
            target.parents('fieldset').find('.field-page').hide();
          } else if ($(e).val() === "1" && e.selected) {
            target.parents('fieldset').find('.field-link').hide();
            target.parents('fieldset').find('.field-page').show();
          }
        }
      });
    });
  });
})(django.jQuery);

toggleFooter = () => {
  const menuType = $('#id_menu_type');
  const options = menuType.find('option');
  const footer = menuType.parents('fieldset').find('.field-footer');
  const formsets = $('.dynamic-navigationlinks_set');

  if (options[1].selected) {
    // options[1] it's a main menu
    footer.css({'display': 'none'});
    formsets.each((i, e) => {
      const target = $(e);
      target.find('.field-phone').hide();
      target.find('.field-page').hide();
      target.find('.field-icon').hide();
      target.find('[id$="-link_to"] option:nth-child(n+3)').hide();
    });
  } else {
    footer.css({'display': 'block'});
  }

  if (options[2].selected) {
    formsets.each((i, e) => {
      const target = $(e);
      target.find('[id$="-link_to"] option').show();
      target.find('.field-phone').hide();
      target.find('.field-icon').hide();
      target.find('[id$="-link_to"] option:nth-child(n+3)').hide();
      target.find('.field-page').show();
    });
  }

  if (options[3].selected) {
    formsets.each((i, e) => {
      const target = $(e);
      target.find('[id$="-link_to"] option').show();
      target.find('.field-phone').hide();
      target.find('.field-page').hide();
      target.find('[id$="-link_to"] option:nth-child(n+2)').hide();
      target.find('.field-icon').show();
    });
  }

  if (options[4].selected) {
    formsets.each((i, e) => {
      const target = $(e);
      target.find('[id$="-link_to"] option').hide();
      target.find('.field-link').hide();
      target.find('.field-icon').hide();
      target.find('.field-page').hide();
      target.find('.field-phone').show();
      target.find('[id$="-link_to"] option:nth-child(3)').show();
    });
  }
};
