<!DOCTYPE html>
<html>
<head>
	<title> Machine Learning Methods</title>
	<meta name='author' content='FranzeJr.' />
	<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
	<link href="jqueryFileTree.css" rel="stylesheet" type="text/css" media="screen" />
	<!-- Page styles -->
	<link type='text/css' href='css/demo.css' rel='stylesheet' media='screen' />
	<link href="style.css" rel="stylesheet" type="text/css" media="screen" />	

	<!-- Contact Form CSS files -->
	<link type='text/css' href='css/basic.css' rel='stylesheet' media='screen' />

	<!-- JS files are loaded at the bottom of the page -->
</head>
<body>
<div id='container'>
	
	<div id='logo'>
		<h1>Machine<span>Learning</span> Algorithms</h1>
		<span class='title'>A small system to work with Machine Learning</span>
	</div>
		
		<div class="example">
			<h2>Implemented Methods</h2>
			<div id="fileTreeDemo_1" class="demo"></div>
		</div>
		
		<div class="example">
			<h2>Inserted Data</h2>
			<div id="fileTreeDemo_2" class="demo"></div>
		</div>
		
		<div class="example">
			<h2>Upload a new data</h2>
			<p>
				You can to upload a new data.
				<a href="#" onclick="openDialogUpload()">Click here</a>
			</p>
		</div>
		
		<div class="example">
			<h2>Execute existed data</h2>
			Click on a list item to choose what you want to use. <br/>

			Method:<div id="method_div"></div>
			Data:<div id="data_div"></div>
		</div>

		<!-- modal content -->
		<div id="basic-modal-content">
			<h5>You can upload your file</h5>
    		<form action="upload_file.php" method="post" enctype="multipart/form-data">
				<label for="file">Filename:</label>
				<input type="file" name="file" id="file"><br>
				<br/>
				<input type="submit" name="submit" value="Upload this file">
			</form>
		</div>

		<!-- preload the images -->
		<div style='display:none'>
			<img src='img/basic/x.png' alt='' />
		</div>
	<div id='footer'>
		Universidade Federal do Ceará, Artificial Inteligence <br/>
		Advisor: Carlos Brito
	</div>
</div>

<!-- Load jQuery, SimpleModal and Basic JS files -->
<script type='text/javascript' src='js/jquery.js'></script>
<script type='text/javascript' src='js/jquery.simplemodal.js'></script>

<script type='text/javascript'>
	
	function Action(method, data){
		this.method = method;
		this.data = data;
	}
	function openDialogUpload(){
		$('#basic-modal-content').modal();
	}
	//Read function
	jQuery(function ($) {
		action = new Action();
		$('#fileTreeDemo_1').fileTree({ root: '/home/franzejrpy/ufc.franzejr.com/disciplinas/ia/methods/', script: 'connectors/jqueryFileTree.php' }, function(file) { 
			var method = file.split("/");
			method = method[method.length-1];
			action.method = method;
			$("#method_div").text(method);
		});
				
		$('#fileTreeDemo_2').fileTree({ root: '/home/franzejrpy/ufc.franzejr.com/disciplinas/ia/data/', script: 'connectors/jqueryFileTree.php', folderEvent: 'click', expandSpeed: 750, collapseSpeed: 750, multiFolder: false }, function(file) { 
			var data = file.split("/");
			data = data[data.length-1];
			action.data = data;
			$("#data_div").text(data);
		});
		
	});	
</script>

<script src="http://gsgd.co.uk/sandbox/jquery/easing/jquery.easing.1.3.js" type="text/javascript"></script>
<script src="jqueryFileTree.js" type="text/javascript"></script>

</body>
</html>