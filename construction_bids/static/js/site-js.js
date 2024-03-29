// site-js.js
$(document).ready(function () {
  function addFormset(formsetContainer) {
    var formset = $("#" + formsetContainer);
    var totalForms = parseInt(formset.find('[name="form-TOTAL_FORMS"]').val());
    var newForm = formset
      .find("." + formsetContainer + "-container:first")
      .clone(true);
    newForm.find("input, select").each(function () {
      var prefix = "form-" + totalForms + "-";
      var newName = $(this)
        .attr("name")
        .replace(/form-\d+-/, prefix);
      $(this).attr({ name: newName, id: newName });
      $(this).val("");
    });
    newForm.appendTo(formset).removeClass("hidden");
    formset.find('[name="form-TOTAL_FORMS"]').val(totalForms + 1);
  }

  $("#add-task").click(function () {
    addFormset("task-formset");
  });

  $("#add-client").click(function () {
    addFormset("client-formset");
  });
});
