$(function () {
  // block handlers start
  const wrappersWithNestedBlocks = [4, 5, 7, 9, 10];
  const searchedArray = ['careers', 'investor'];
  const sets = $('#pageblock_set-group, #news_set-group, #vacancy_set-group, #review_set-group');

  sets.fadeOut(500);

  const blockType = $('#id_block_type');
  const blockOptions = blockType.find('option');

  blockOptions.filter((i, e) => {
    handleFormSets(e, sets, wrappersWithNestedBlocks);
  });

  $(document).on('change', '#id_block_type', (el) => {
    // toggle blocks due to selected option
    $(el.currentTarget).find('option').filter((i, e) => {
      handleFormSets(e, sets, wrappersWithNestedBlocks);
    })
  });
  // block handlers end

  // nested blocks handlers start
  const nestedBlocks = $('#pageblock_set-group');
  const nestedItems = nestedBlocks.find('[id^="pageblock_set"]:not([id$="empty"])');
  nestedItems.each((i, e) => {
    $(e).find('[id$="-block_type"]').find('option:not(:last-child)').hide();
  });
  $(document).on('click', '#pageblock_set-group .add-row', () => {
    const elements = nestedBlocks.find('[id^="pageblock_set-"]:not([id$="empty"])');
    elements.each((i, e) => {
      $(e).find('[id$="-block_type"]').find('option:not(:last-child)').hide();
    });
  });
  $(document).on('change', '[id^="pageblock_set"] [id$="-block_type"]', (e) => {
    const target = $(e.currentTarget);
    const searchedValue = blockType.find(`option[value="${blockType.val()}"]`).text().split('_')[0];
    // console.log(searchedArray.includes(searchedValue));
    if (searchedValue === 'investor') {
      const $iframe = target.parents('.field-block_type').parent().find('iframe.cke_wysiwyg_frame');
      let root = false;

      $.ajax({
          type: 'GET',
          url: `/template/fetch/${searchedValue}/`,
        })
          .done(resp => {
          const data = resp.html;
          $iframe.ready(() => {
            // Fill content field with data;
            $iframe.contents().find('body').html('');
            $iframe.contents().find('body').append(data);
            if (root === false) {
              root = true;
              const showBlocks = $('a.cke_button__showblocks');
              showBlocks.click();
              const source = $('a.cke_button__source');
              source.click();
              setTimeout(() => {
                source.click();
              }, 500);
            }
          });
        });
    }
  });
  // nested blocks handlers end

  // vacancies block handlers start
  $(document).on('click', '#vacancy_set-group .add-row', () => {
    const elements = $('#vacancy_set-group').find('[id^="vacancy_set-"]:not([id$="empty"])');
    const last = $(elements[elements.length - 1]);
    setTimeout(() => {
      const description = last.find('fieldset').children();
      const $iframe = $(description[0]).find('iframe.cke_wysiwyg_frame');
      let root = false;
      $.ajax({
          type: 'GET',
          url: `/template/fetch/careers/`,
        })
          .done(resp => {
          const data = resp.html;
          $iframe.ready(() => {
            // Fill content field with data;
            $iframe.contents().find('body').html('');
            $iframe.contents().find('body').append(data);
            if (root === false) {
              root = true;
              const showBlocks = $(description[0]).find('a.cke_button__showblocks');
              showBlocks.click();
              const source = $(description[0]).find('a.cke_button__source');
              source.click();
              setTimeout(() => {
                source.click();
              }, 500);
            }
          });
        });
    }, 500);
  });
  // vacancies block handlers end

  // navigationLinks handlers start
  const navLinksBlock = $('#navigationlinks_set-group');
  const navItems = navLinksBlock.find('[id^="navigationlinks_set"]:not([id$="empty"])');
  if (navItems.length > 1) {
    navLinksBlock.find('.add-row').hide();
  } else {
    navLinksBlock.find('.add-row').show();
  }
  navItems.each((i, e) => {
    const target = $(e);
    target.find('.field-navigation').hide();
    target.find('.field-icon').hide();
    target.find('.field-phone').hide();
    target.find('.field-use_in_slider').hide();
    target.find('.field-slider_item').hide();
    target.find('.field-link_to').find('select option[value="2"]').hide();
    target.find('.field-link_to').find('select option[value="3"]').hide();
    if (+target.find('.field-link_to').find('select').val() === 0) {
      target.find('.field-page').hide();
    } else if (+target.find('.field-link_to').find('select').val() === 1) {
      target.find('.field-link').hide();
    }
  });
  $(document).on('click', '#navigationlinks_set-group .add-row', (el) => {
    const elements = navLinksBlock.find('[id^="navigationlinks_set"]:not([id$="empty"])');
    if (elements.length > 1) {
      $(el).hide();
    } else {
      $(el).show();
    }
    elements.each((i, e) => {
      const target = $(e);
      target.find('.field-navigation').hide();
      target.find('.field-icon').hide();
      target.find('.field-phone').hide();
      target.find('.field-use_in_slider').hide();
      target.find('.field-slider_item').hide();
      target.find('.field-link_to').find('select option[value="2"]').hide();
      target.find('.field-link_to').find('select option[value="3"]').hide();
    });
  });
  $(document).on('change', '[id^="navigationlinks_set"] [id$="-link_to"]', (e) => {
    const target = $(`#${e.currentTarget.id}`);
    if (+target.val() === 0) {
      target.parents('.field-link_to').parent().find('.field-page').fadeOut(500);
      target.parents('.field-link_to').parent().find('.field-link').fadeIn(500);
    } else if (+target.val() === 1) {
      target.parents('.field-link_to').parent().find('.field-link').fadeOut(500);
      target.parents('.field-link_to').parent().find('.field-page').fadeIn(500);
    }
    // target.find()
  });
  // navigationLinks handlers end

  // slider handlers start
  const sliderGroup = $('#slider_set-group');
  const sliderItems = sliderGroup.find('[id^="slider_set"]:not([id$="empty"]');
  if (sliderItems.length > 0) {
    sliderGroup.find('.add-row').hide();
  } else {
    sliderGroup.find('.add-row').show();
  }

  const useSlider = $('#id_use_slider');
  if (!useSlider[0].checked) {
    sliderGroup.fadeOut();
  }

  $(document).on('click', '#id_use_slider', (e) => {
    // handle slider formset section
    const target = e.currentTarget;
    if (target.checked) {
      sliderGroup.fadeIn(500);
    } else {
      sliderGroup.fadeOut(500);
      sliderGroup.find('fieldset.module.aligned > [name^="slider_set-"]').filter((i, e) => {
        if (e.tagName === 'SELECT') {
          $(e).find('option').removeAttr('selected');
          $(e).find('option:first-child').attr('selected', 'selected');
        }
        e.value = undefined;
      });
    }
  });
  // slider handlers end

});

handleFormSets = (e, sets, wrappersWithNestedBlocks) => {
  if (e.selected && e.value) {
    sets.fadeOut(500);

    if (+e.value === 0) {
      $('#vacancy_set-group').fadeIn(500);
      $('.field-use_slider').fadeOut(500);
    } else if (+e.value === 1) {
      $('#news_set-group').fadeIn(500);
    } else if (wrappersWithNestedBlocks.includes(+e.value)) {
      $('#pageblock_set-group').fadeIn(500);
    } else if (+e.value === 6) {
      $('.field-use_slider').fadeIn(500);
    } else if (+e.value === 8) {
      $('#review_set-group').fadeIn(500);
      $('.field-use_slider').fadeIn(500);
    }
    // else if (+e.value === 11) {
    //   $('#pageblock_set-group').fadeIn(500);
    // }
  }
};
