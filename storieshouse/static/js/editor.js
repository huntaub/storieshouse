$(document).ready(function() {
	$(".i-preview i").hide();
	var last_icon = "";
	var editor = new EpicEditor({textarea: "id_body", basePath: "/static", clientSideStorage: false}).load();
	image = $("#id_image").change(function() {
		if($("#id_image").val() != "") {
			$("#id_icon").val("");
			$(".i-preview i").hide();
			$(".i-preview img").show();
			$(".i-preview img").attr("src", $("#id_image").val());
		} else {
			$(".i-preview img").attr("src", "https://s3.amazonaws.com/storiestime/sh-default.png");
		}
	});
	icon = $("#id_icon").change(function () {
		if($("#id_image").val() == "") {
			$(".i-preview img").hide();
			$(".i-preview i").show();
			$(".i-preview i").removeClass(last_icon);
			var new_icon = ("fa-" + $("#id_icon").val());
			$(".i-preview i").addClass(new_icon);
			last_icon = new_icon;
		}
	});
});