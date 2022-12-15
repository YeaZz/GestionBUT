
	var contactbutton = document.getElementById('submit');
	var namee = document.getElementById('name-error');

	function containsNumbers(str) {
		return /[0-9]/.test(str);
	}

	function subsubmit(){
		console.log('verification apply');
		
		if(document.getElementById('firstname').value == ''){
			namee.innerHTML = 'champ obligatoire';
		} else if(containsNumbers(document.getElementById('firstname').value)){
			namee.innerHTML = 'Erreur de saisie';
		} else{
			namee.innerHTML = '';
		}

	}