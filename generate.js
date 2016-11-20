function addElementLi(obj){
	var ul = document.getElementById(obj);
	var li = document.createElement("li");
	li.setAttribute("id", "newli");
	li.innerHTML = "js动态添加的li";
	ul.appendChild(li);
}

function addElementImg(obj){
	var ul = document.getElementById(obj);
	var li = document.createElement("li");
	var img = document.createElement("img");
	img.setAttribute("id", "newImg");
	img.src = "./image/someimage.jpg";
	li.appendChild(img);
	ul.appendChild(li);
	
}
function getFileInFolder(path){
	var fso = new ActiveXObject("Scripting.FileSystemObject");
	
	// var file1 = fso.createtextfile("./myjsfile.txt", true);
	
	// var file2 = fso.GetFile("./myjsfile.txt");
	// alert("file last modified: " + file2.DateLastModified);
	
	// fso.CreateFolder("d:\\jsfolder");
	
	var folder = fso.GetFolder(path);
	var files = new Enumerator(folder.Files);
	
	for(; !files.atEnd(); files.moveNext()){
		file = files.item();
		document.write("type: " + file.type + " name: " + file.name + "<br/>");
	}
		
}


