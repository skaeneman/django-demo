// site-js.js
$(document).ready(function () {
  function addFormset(formsetContainer, prefix) {
    var formset = $("#" + formsetContainer);
    var totalFormElName = prefix + "-TOTAL_FORMS";
    var totalForms = parseInt(
      formset.find("[name=" + totalFormElName + "]").val()
    );
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
    formset.find("[name=" + totalFormElName + "]").val(totalForms + 1);
  }

  $("#add-task").click(function () {
    addFormset("task-formset", "tasks");
  });

  $("#add-client").click(function () {
    addFormset("client-formset", "clients");
  });
});
