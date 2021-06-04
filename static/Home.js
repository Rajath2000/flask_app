// file size checker
var uploadField = document.getElementById("Proof");

uploadField.onchange = function() {
    if(this.files[0].size > 1048576){
       alert("File is too big! shoud be less than 1mb");
       this.value = "";
    };
};


function formValidator()
{
var usn = document.getElementById('USN');
usnExp=/[1-4][A-Z][A-Z]\d{2}[A-Z][A-Z]\d{3}$/
if(usn.value.length==0)
{
alert("USN is empty.");
usn.focus();
return false;
}
else if(!usn.value.match(usnExp))
{
alert("USN should be in VTU USN format, eg., 1GD10CS001");
usn.focus();
return false;
}

};
// usnvaidator

//clear action
function myFunction() {
    document.getElementById("myForm").reset();
  }


//FID formValidator
function formValidatorFID()
    {
        var FID = document.getElementById('FID');
        fidExp=/[A-Z][A-Z]\d{3}$/
        if(FID.value.length==0)
        {
        alert("FID is empty.");
        FID.focus();
        return false;
        }
        else if(!FID.value.match(fidExp))
        {
        alert("USN should be in VTU USN format, eg., FA788");
        usn.focus();
        return false;
        }

    };

