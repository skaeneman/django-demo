// let formsetContainer = document.querySelectorAll('.formset-container'),
// form = document.querySelector('#form'),
// addFormsetButton = document.querySelector('#add-formset'),
// totalForms = document.querySelector('#id_form-TOTAL_FORMS'),
// formsetNum = formsetContainer.length - 1; // Returns the Number of the Last Form on the Page, where index starts at zero

// // console.log(totalForms);

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

const addMoreBtn = document.getElementById('add-more');
const totalNewForms = document.getElementById('id_form-TOTAL_FORMS');

// count the number of classes with the name 'client-formset-container' so we can get the total number of forms
const currentClientForms = document.getElementsByClassName('client-formset-container');

addMoreBtn.addEventListener('click', add_new_form);

function add_new_form(event) {
  if (event) {
    // don't allow form to be submitted yet
    event.preventDefault();
  }

  // increment the total number of forms
  const currentFormCount = currentClientForms.length //+ 1;
  console.log(currentFormCount);

  // where form will be copied to
  const formCopyTarget = document.getElementById('client-list');
  // make a copy of the original empty form
  const copyEmptyformElement = document.getElementById('empty-form').cloneNode(true);
  copyEmptyformElement.setAttribute('class', 'client-formset-container');
  copyEmptyformElement.setAttribute('id', `client-form-${currentFormCount}`);

  // replace all instances of '__prefix__' with the current form count
  const regex = new RegExp(`__prefix__`, 'g');
  copyEmptyformElement.innerHTML = copyEmptyformElement.innerHTML.replace(regex, currentFormCount);

  // TODO: FIX THIS 
  // totalNewForms.setAttribute('value', currentFormCount + 1); // increment the number of total forms in the management form data

  formCopyTarget.append(copyEmptyformElement); // add the copy to the end of the list
}