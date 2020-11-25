function printFileNames(el){
    var files = el.files;
    
    var ul = document.getElementById("filenames");
    ul.innerHTML = '';
    var totalSize = 0; // MB
    var totalSizeTxt = "Total size - ";

    for(var i=0; i<files.length; i++){
        var fileSize = files[i].size*Math.pow(10, -6);
        totalSize += fileSize;
        
        var li = document.createElement("li");
        li.appendChild(document.createTextNode("Filename: "+files[i].name+" - File size: "+fileSize+" MB"));
        ul.appendChild(li);
    }
    
    totalSizeTxt += totalSize+"MB";
    document.getElementById('totalSize').innerHTML = totalSizeTxt;

    if (totalSize > 25){
        alert("Total size bigger than 25MB. Re-upload a smaller total size.");
        ul.innerHTML='';
        el.value = null;
        document.getElementById('totalSize').innerHTML = "Total size - 0MB";
    }
}