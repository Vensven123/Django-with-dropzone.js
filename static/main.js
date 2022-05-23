Dropzone.autoDiscover = false;

let my_Dropzone = new Dropzone("#zone",{

    url:'upload/',                 // file path
    maxFiles: 2,                   //count
    maxFilesize:  2,               // MB
    acceptedFiles :'.png, .jpg',   // file type

})
