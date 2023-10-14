<script>
   // import entire JSON file as a default import
   import { question } from '$lib/data/testPrompt.json';

   // import root level object as a named import
   import { answer } from '$lib/data/testPrompt.json';
   import QuestionBlock from '../QuestionBlock.svelte';



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
   for (let i = 0; i < answerChoicesAndQuestion.length; i++) {
       for (let j = 0; j < answerChoicesAndQuestion[0].length; j++) {
        const element = answerChoicesAndQuestion[i][j];
        console.log(element);
       }
   }
   console.log(answerChoicesAndQuestion[0][2]);
 </script>

<h> Testing out the page component </h>
<QuestionBlock question={answerChoicesAndQuestion[0][0]}, answerChoice1={answerChoicesAndQuestion[0][1]}, answerChoice2={answerChoicesAndQuestion[0][2]}, answerChoice3={answerChoicesAndQuestion[0][3]}, answerChoice4={answerChoicesAndQuestion[0][4]}/>
<QuestionBlock question={answerChoicesAndQuestion[1][0]}, answerChoice1={answerChoicesAndQuestion[1][1]}, answerChoice2={answerChoicesAndQuestion[1][2]}, answerChoice3={answerChoicesAndQuestion[1][3]}, answerChoice4={answerChoicesAndQuestion[1][4]}/>
<QuestionBlock question={answerChoicesAndQuestion[2][0]}, answerChoice1={answerChoicesAndQuestion[2][1]}, answerChoice2={answerChoicesAndQuestion[2][2]}, answerChoice3={answerChoicesAndQuestion[2][3]}, answerChoice4={answerChoicesAndQuestion[2][4]}/>
