videojs.registerPlugin('endScreenPlugin', function() {
	var player = this;
	player.on("ended",function(){
		player.posterImage.el().style.display = 'inline-block';
        if (player.posterImage.el().firstChild) player.posterImage.el().firstChild.style.display = 'inline-block';
		player.bigPlayButton.el().style.display = 'block';
	})
	player.on("play",function(){
		player.posterImage.el().style.display = 'none';
		player.bigPlayButton.el().style.display = 'none';
	})
});