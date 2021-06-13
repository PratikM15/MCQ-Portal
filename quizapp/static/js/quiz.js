function submitForm(e){
    e.preventDefault();
    let name = document.forms["welcome_form"]["examieeName"].value;

    // store examieeName
    sessionStorage.setItem('name',name);

    location.href = "quiz.html"
    console.log(name)
}

let question_count =  0;

function next(){
    question_count++;
    connsole.log(question_count)
}

function show(count){
    let question = document.getElementById('questions');
    question.innerHTML = questions.id;
}