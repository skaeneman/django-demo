// let formsetContainer = document.querySelectorAll('.client-formset-container'),
// form = document.querySelector('#form'),
// addFormsetButton = document.querySelector('#add-more'),
// totalForms = document.querySelector('#id_client_set-TOTAL_FORMS'),
// formsetNum = formsetContainer.length - 1; // Returns the Number of the Last Form on the Page, where index starts at zero

// console.log(formsetContainer);

// addFormsetButton.addEventListener('click', $addFormset);

// function $addFormset(e) {
// e.preventDefault();

// let newForm = formsetContainer[0].cloneNode(true), // Clone the formsetContainer
//     formRegex = RegExp(`form-(\\d){1}-`,'g'); // Regex to find all instances of form-{{ # }} in the string of all internal HTML

// formsetNum++ // Increment the Form Number
// newForm.innerHTML = newForm.innerHTML.replace(formRegex, 'form-${formsetNum}-'); // Update the new Form to have the Correct Form Number in the string of internal HTML, such as name or class attributes
// form.insertBefore(newForm, addFormsetButton); // Insert the new form at the end of the list of forms, just before the add new form button

// totalForms.setAttribute('value', '${formsetNum + 1}'); // Increment the Number of Total Forms in the Management Form Data
// }



$(document).ready(function () {

    /*
    * Add a new form to the formset
    * @param {string} formsetContainer - the CSS class name of the formset container
    * @param {string} formsetList - the CSS id name of the formset list where the new form will be appended
    * @param {string} emptyFormId - the CSS id name of the empty form that will be copied
    * @param {string} modelPrefix - name used in the auto created django management_form data (e.g. id_client_set-TOTAL_FORMS).
    *                               if id_client_set-TOTAL_FORMS is the management_form, then modelPrefix would just be 'client_set' 
    */
    function addNewFormset(formsetContainer, formsetList, emptyFormId, modelPrefix) {
      // remove '_set' from the modelPrefix so we can get the model name (e.g. client_set -> client)
      let modelName = modelPrefix;
      if (modelName.includes("_set")) {
        modelName = modelName.replace("_set", "");
      }

      const totalNewForms = document.getElementById('id_'+ modelName +'_set-TOTAL_FORMS');

      // count the number of classes named '<something>-formset-container' so we can get the total number of forms on the page
      const currentForms = document.getElementsByClassName(formsetContainer);    
      
      // if (event) {
      //   // don't allow form to be submitted yet
      //   event.preventDefault();
      // }
      
      // get the number of forms on the page
      const currentFormCount = currentForms.length;
      console.log(currentFormCount);

      // where the new form will be appened to
      const formCopyTarget = document.getElementById(formsetList);

      // make a copy of the original empty form and set its class and unique id
      const copyEmptyformElement = document.getElementById(emptyFormId).cloneNode(true);
      copyEmptyformElement.setAttribute('class', formsetContainer);

      // set the unique id of the new form (e.g. client-form-1, client-form-2, etc.)
      copyEmptyformElement.setAttribute('id', modelName + `-form-${currentFormCount}`);

      // replace all instances of '__prefix__' with the current form count
      const regex = new RegExp(`__prefix__`, 'g');
      copyEmptyformElement.innerHTML = copyEmptyformElement.innerHTML.replace(regex, currentFormCount);

      // increment the number of total forms in the management_form data
      totalNewForms.setAttribute('value', currentFormCount + 1);
      console.log(modelPrefix + "count: ", totalNewForms.getAttribute('value'));

      // add the new copy to the end of the list
      formCopyTarget.append(copyEmptyformElement);
    }

    // add a new form when the add button is clicked
    $("#add-task").click(function () {
      addNewFormset("task-formset-container", "task-list", "empty-task-form", "task_set")    
    });

    $("#add-client").click(function () {
      addNewFormset("client-formset-container", "client-list", "empty-client-form", "client_set")    
    });

});