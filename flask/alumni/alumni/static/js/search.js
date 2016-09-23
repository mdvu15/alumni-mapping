$(function() {
	$('#search_button').bind('click',
		function() {
			$('#map').css({"float":"left", "width":"68%"});
			$('#ainfo').css({"float":"right", "display":"inline"});
			$('#ainfo').show();
			$.getJSON($SCRIPT_ROOT + '/_search', {
				zip: $('input[name="zip"]').val()
			}, function(data) {
				$('span#search_zip').text(data.result[0].zipcode);
				for (var i = 0; i<data.result.length; i++) {
					var j = $("<li> </li>").text(data.result[i].first_name + " " + data.result[i].last_name);
					$('#search_result').append(j);
				};
			});
		return false;
	});
});
