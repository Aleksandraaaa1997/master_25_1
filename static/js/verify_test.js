var currentTime = document.getElementById('total_time').value * 60;
var submit_btn = document.getElementById('submit-btn');

// Function to update the timer display
function updateTimer() {

    var minutes = Math.floor(currentTime / 60);
    var seconds = currentTime % 60;

    // Display the time in the format MM:SS
    document.getElementById('timesWatch').innerHTML = (minutes < 10 ? '0' : '') + minutes + ':' + (seconds < 10 ? '0' : '') + seconds;

    if (currentTime == 0){
    submit_btn.click();

    }
}

updateTimer()
function toggleHelp(questionId, pomocIndex, len) {
    console.log('Attempting to access pomoc_vidljiva element:', 'pomoc_vidljiva_' + questionId + '_' + pomocIndex);
    console.log('Attempting to access help element:', 'pomoc_' + questionId + '_' + pomocIndex);
    setujNivoPomoci(questionId,pomocIndex+1)
    var pomocVidljivaElement = document.getElementById('pomoc_vidljiva_' + questionId + '_' + pomocIndex);
    pomocVidljivaElement.style.display = 'block';
    var pomocElement = document.getElementById('pomoc_' + questionId + '_' + pomocIndex);
    pomocElement.style.display = 'none';
    console.log('Attempting to access help element:', 'pomoc_' + questionId + '_' + (pomocIndex+1));
    if(pomocIndex<len-1){
    var pomocElement = document.getElementById('pomoc_' + questionId + '_' + (pomocIndex+1));
    pomocElement.style.display = 'block';
    } else if(pomocIndex==len-1){
    var resenjeElement = document.getElementById('resenje_' + questionId);
    resenjeElement.style.display = 'block';
    }
}


function disableRadioInputs() {
    var radioInputs = document.querySelectorAll('input[type="radio"]');

    for (var i = 0; i < radioInputs.length; i++) {
        radioInputs[i].disabled = true;
    }
}
checkEvt();

function prikaziResenje(questionId) {
    var resenjeElement = document.getElementById('resenje_' + questionId);
    resenjeElement.setAttribute('clicked','True');
    setujNivoPomoci(questionId,10)
    window.open('/solution/'+questionId, '_blank');
}

function setujNivoPomoci(questionId,nivo) {
    // Send an AJAX request to the server to record the click
    fetch('/record_help/'+questionId, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ help_level: nivo })
    });
}
function collectResults(questions,button){

    clearInterval(timerInterval);
    fetch('/record_time', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ total_time: currentTime })
    });
    button.disabled = true;
    button.style.backgroundColor = '#FFB534';
    for (var i = 0; i < questions.length; i++) {
            var radioButtons = document.getElementsByName("question_"+questions[i].id);
            radioButtons.forEach(function(radioButton) {
            if (radioButton.checked) {
                var backgroundColor = radioButton.value==questions[i].correct_answer ? '#A6FF96' : '#FF6D60';
                radioButton.parentNode.style.backgroundColor = backgroundColor;
            }
        });
    }
    console.log('pauza');
    // Submit the form
    form.target = '_blank';
    form.submit();
    disableRadioInputs();
}
function refreshPage() {
    location.href = location.href;  // Reloads the current document
}
