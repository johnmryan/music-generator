var app = angular.module('musicApp',[]);
app.controller('MusicController', ['$scope', function($scope) {
	var vm = this;
	vm.notes = undefined;
	vm.order = "first";
	vm.generated_songs = undefined;
	var frequencies = new Array();
	frequencies['C'] = 261.63;
	frequencies['D'] = 293.66;
	frequencies['E'] = 329.63;
	frequencies['F'] = 349.23;
	frequencies['G'] = 392.00;
	frequencies['A'] = 440.00;
	frequencies['B'] = 493.88;

	vm.generate = function() {
		if (vm.notes) {
			var music = vm.notes;
			if (vm.order === "first") {
				var markov_dict = build_markov_dict(music);
				var scores = [];
				for (var i=0;i<10;i++) {
					var score = generate_score(markov_dict);
					scores.push(score);
				}
				scores.pop();
				vm.generated_songs = scores;
			}
			else {
				//build_so(music);
			}
		}
	}

	//Helper functions
	function random_choice(choices) {
		var index = Math.floor(Math.random() * choices.length);
		return choices[index];
	}

	function build_markov_dict(s) {
		// Builds a dictionary using input string
		var markov_dict = new Array();
		for (var i=0; i < s.length; i++) {
			if (!(s[i] in markov_dict)) {
				markov_dict[s[i]] = [s[i+1]];
			}
			else {
				markov_dict[s[i]].push(s[i+1]);
			}
		}
		return markov_dict;
	}
	
	function build_charset(notes) {
		char_set = {};
		for (var i=0; i < notes.length; i++) {
			if (!(notes[i] in char_set)) {
				char_set[notes[i]] = true;
			}
		}
		var keys = [];
		for (k in char_set) {
			if (char_set.hasOwnProperty(k)) {
				keys.push(k);
			}
		}
		keys.sort();
		return keys;
	}

	function generate_score(markov_dict) {
		//return most frequent
		var most_freq = Object.keys(markov_dict)[0];
		var len = markov_dict[most_freq].length;
		for (key in markov_dict) {
			if (markov_dict[key].length > len) {
				most_freq = key;
				len = markov_dict[key].length;
			}
		}
		var current = most_freq;
		var score = [current];
		var i = 0;
		while (current in markov_dict && i < 30) {
			c = random_choice(markov_dict[current]);
			score.push(c);
			current = c;
			i++;
		}
		return score;
	}
	
}]);
