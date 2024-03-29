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
    newForm.find(".errorlist").remove();
    newForm.find("input, select").each(function () {
      var prefix = modelPrefix + "-" + totalForms + "-";
      var reg = new RegExp(modelPrefix + "-\\d+-");

      var newName = $(this).attr("name").replace(reg, prefix);
      $(this).attr({ name: newName, id: newName });
      $(this).val("");

      if ($(this).is(":checkbox")) {
        $(this).prop("checked", false);
        $(this).removeAttr("checked"); // Uncheck the checkbox
      }
    });
    newForm.find("label").each(function () {
      var prefix = modelPrefix + "-" + totalForms + "-";
      var reg = new RegExp(modelPrefix + "-\\d+-");

      var newName = $(this).attr("for").replace(reg, prefix);
      $(this).attr({ for: newName });
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

  $('#form').submit(function(event) {
    var formsets = ["task-formset", "client-formset"];
    formsets.forEach(function(formsetID) {
      // Iterate over delete checkboxes in the current formset
      $('#' + formsetID + ' input[type="checkbox"]').each(function () {
        // If the checkbox is checked, set its value to "on"
        if ($(this).is(':checked')) {
          $(this).val('on');
        } else {
          // If the checkbox is unchecked, ensure its value is not included in the form data
          $(this).prop('disabled', true);
        }
      });
    });

  });

});
