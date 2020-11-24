(function($) {
  'use strict';
  $(document).ready(() => {
    let first = null;
    let root = false;

    $(document).on('change', '#id_block_type', (e) => {
      const target = $(e.currentTarget);
      const selectVal = target.val();
      const option = target.find(`option[value="${selectVal}"]`);
      const selectedTemplate = option.text();
      let agree = false;
      if (first !== null) {
        agree = confirm('Are you sure that you want to change content structure?');
        if (!agree) {
          $(e.currentTarget).val(first);
          return;
        }
      }
      first = selectedTemplate;
      const $iframe = $('iframe.cke_wysiwyg_frame');

      // if (selectedTemplate !== '') {
      //   $.ajax({
      //     type: 'GET',
      //     url: `/template/fetch/${selectedTemplate}/`,
      //   })
      //     .done(resp => {
      //     const data = resp.html;
      //     $iframe.ready(() => {
      //       // Fill content field with data;
      //       $iframe.contents().find('body').html('');
      //       $iframe.contents().find('body').append(data);
      //       if (root === false) {
      //         root = true;
      //         const showBlocks = $('a.cke_button__showblocks');
      //         showBlocks.click();
      //         const source = $('a.cke_button__source');
      //         source.click();
      //         setTimeout(() => {
      //           source.click();
      //         }, 500);
      //       }
      //     });
      //   });
      // } else {
      //   $iframe.ready(() => {
      //     // Clear content field
      //     $iframe.contents().find('body').html('');
      //   });
      // }
    });
  });
})(django.jQuery);
