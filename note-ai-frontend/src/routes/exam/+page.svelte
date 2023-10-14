<script>
   // import entire JSON file as a default import
   import { question } from '$lib/data/testPrompt.json';

   // import root level object as a named import
   import { answer } from '$lib/data/testPrompt.json';



   const questionString = question;
   const answerString = answer;
   console.log(questionString);
   console.log(answerString);
   const questions = questionString.split("\n\n");
   let answerChoicesAndQuestion = new Array();
   questions.forEach((q) => {
       answerChoicesAndQuestion.push(q.split("\n"))});
   console.log(questions);
   answerChoicesAndQuestion.forEach((q) => {
       console.log(q);
   });
   console.log(answerChoicesAndQuestion[0][2]);
 </script>

<h> Testing out the page component </h>
