var selectedRow = null;
function onFormSubmit() {
var formData = readFormData();
if(isValid()){
    if (selectedRow == null) {
    insertNewRecord(formData);
    alert("Your details are saved Sucessfully........");
  }
 else{
  updateRecord(formData);
 }
  resetForm();
}
}

function readFormData() {
  var formData = {};
  formData["studentName"] = document.getElementById("studentName").value;
  formData["studentCollage"] = document.getElementById("studentCollage").value;
  formData["studentCourse"] = document.getElementById("studentCourse").value;
  return formData;
("studentAge").value;
  formData["studentAge"] = document.getElementById("studentAge").value;
  return formData;
("studentPlace").value;
  formData["studentPlace"] = document.getElementById("studentPalce").value;
  return formData;
}
function resetForm() {
  document.getElementById("studentName").value = "";
  document.getElementById("studentCollage").value = "";
  document.getElementById("studentCourse").value = "";
  selectedRow = null;
}
function insertNewRecord(data) {
  var table = document
    .getElementById("studentlist")
    .getElementsByTagName("tbody")[0];
  var newRow = table.insertRow(table.length);
  cell1 = newRow.insertCell(0);
  cell1.innerHTML = data.studentName;
  cell2 = newRow.insertCell(1);
  cell2.innerHTML = data.studentCollage;
  cell3 = newRow.insertCell(2);
  cell3.innerHTML = data.studentCourse;
  cell4 = newRow.insertCell(5);
  cell4.innerHTML = `<a onClick="onEdit(this)">Update</a><a onClick="onDelete(this)">Delete</a>`;
}
function onEdit(td)
{if(confirm("Are you upadate your details")){
selectedRow=td.parentElement.parentElement;  
document.getElementById("studentName").value=selectedRow.cells[0].innerHTML;
document.getElementById("studentCollage").value=selectedRow.cells[1].innerHTML;
document.getElementById("studentCourse").value=selectedRow.cells[2].innerHTML;
}
}
function updateRecord(formData)
{
  alert("Your form updated sucessfully.......")
selectedRow.cells[0].innerHTML=formData.studentName;
selectedRow.cells[1].innerHTML=formData.studentCollage;
selectedRow.cells[2].innerHTML=formData.studentCourse;
}
function onDelete(td)
{
if(confirm("are you want to delete this record")){
  row=td.parentElement.parentElement;
  document.getElementById("studentlist").deleteRow(row.rowIndex);
  resetForm();
}
}

function isValid(){
var a=document.getElementById("studentName").value;
// var  b = document.getElementById("studentCollage").value;
// var c= document.getElementById("studentCourse").value;
// var d= document.getElementById("studentAge").value;
//  var e= document.getElementById("studentPlace").value;
if(a==""|| a==null ){return false;}
else
{return true;}

}
