$(document).ready(function() {
	$('#search').click( function(e) {
		e.preventDefault();
		e.stopPropagation();
		
		if ($('#surface').val() == '' && $('#lForm').val() == '') {
			$('#message').text('検索文字列を入れてください');
			$("#message").attr("class","alert alert-warning");
			$('#message').show();
		} else {
			
			$('#message').text('検索中です…');
			$("#message").attr("class","alert alert-warning");
			$('#message').show();
			$('#result_tbody').empty();
			
			$.getJSON('web.py', {
				'surface': $('#surface').val(),
				'lForm': $('#lForm').val(),
			}, function(result) {
				
				//$('#count').text(result.length);
				for (var i in result) {
					$('#result_tbody').append($('<tr>'));
					for (j in result[i]) {
						$('#result_tbody tr:last-child').append($('<td>').append(result[i][j]))
					}
				}
				
				if (result.length > 0) {
					$('#message').text(result.length + '件の結果が見つかりました。');
					$("#message").attr("class","alert alert-success");
				} else {
					$('#message').text('見つかりませんでした。');
					$("#message").attr("class","alert alert-success");
				} 
			});
			// alert('ごめんまだ作ってない');	
		}
		
	});
});