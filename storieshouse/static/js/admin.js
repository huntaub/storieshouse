$(document).ready(function() {
	$(".toggle-auctions").click(function(e) {
		$("#auctions").slideToggle();
		e.preventDefault();
	});
});

// Weekdays to Use for Graph Labels
var weekday=new Array(7);
weekday[0]="Sunday";
weekday[1]="Monday";
weekday[2]="Tuesday";
weekday[3]="Wednesday";
weekday[4]="Thursday";
weekday[5]="Friday";
weekday[6]="Saturday";

// Creates a Graph of Views for the Past Week
function createGraph(elem, data, bids) {
	var graph = new Rickshaw.Graph( {
		element: document.querySelector(elem),
		renderer: "line",
		// width: $(elem).width(), 
		height: 173, 
		series: [{
				name: "Views",
				color: 'steelblue',
				data: data,
			},
			{
				name: "Bids",
				color: 'red',
				data: bids,
			}]
		});
	var x_axis = new Rickshaw.Graph.Axis.Time( { graph: graph } );

	// var y_axis = new Rickshaw.Graph.Axis.Y( {
	//  graph: graph,
	//  orientation: 'left',
	//  tickFormat: Rickshaw.Fixtures.Number.formatKMBT,
	//  element: $(elem).siblings(".y-axis")[0],
	// } );
	graph.render();
	var hoverDetail = new Rickshaw.Graph.HoverDetail( {
		graph: graph,
		xFormatter: function(x) {
			if (x == -1) {
				return "Yesterday";
			} else if (x < -1) {
				var d = new Date();
				var n = d.getDay();
				n += x;
				if (n<0)
					n += 7;
				return weekday[n];
			} else if (x == 0) {
				return "Today;"
			}
		},
		yFormatter: function(y) { return y; }
	} );
	$(window).resize(function() {
		graph.width = $(elem).width();
		graph.render();
	});
}