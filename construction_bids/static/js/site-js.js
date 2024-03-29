// site-js.js
$(document).ready(function () {
  function addFormset(formsetContainer, modelPrefix) {
    var formset = $("#" + formsetContainer);
    var totalFormElName = modelPrefix + "-TOTAL_FORMS";
    var totalForms = parseInt(
      formset.find("[name=" + totalFormElName + "]").val()
    );
    var newForm = formset
      .find("." + formsetContainer + "-container:first")
      .clone(true);
    newForm.find("input, select").each(function () {
      var prefix = modelPrefix + "-" + totalForms + "-";
      var reg = new RegExp(modelPrefix + "-\\d+-");

      var newName = $(this).attr("name").replace(reg, prefix);
      $(this).attr({ name: newName, id: newName });
      $(this).val("");
    });
    newForm.appendTo(formset).removeClass("hidden");
    formset.find("[name=" + totalFormElName + "]").val(totalForms + 1);
  }

  $("#add-task").click(function () {
    addFormset("task-formset", "tasks");
  });

  $("#add-client").click(function () {
    addFormset("client-formset", "clients");
  });
});
