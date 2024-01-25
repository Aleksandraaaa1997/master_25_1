// Get the HTML content
var htmlBodyContent = document.body.innerHTML;
var title = document.getElementById('title').textContent
var professor_email = document.getElementById('professor_email').value
// Use the Fetch API to send the HTML content to the Flask server
//fetch('/send_pdf_results', {
//    method: 'POST',
//    headers: {
//        'Content-Type': 'application/json',
//    },
//    body: JSON.stringify({ html_content: htmlBodyContent,title:title, professor_email:professor_email }),
//});

