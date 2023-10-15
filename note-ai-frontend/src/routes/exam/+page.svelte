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

   let showAnswers = false;
 </script>

<div class="bg-cover flex justify-center items-center w-screen h-screen" style="background-image: url('/src/lib/v602-nunoon-32-rippednotes.jpg'); height: 900px">
<div class="w-3/4 h-[60rem] bg-white relative rounded-lg flex flex-col justify-center items-center border-sky-400 border-[18px]">
<h1 class="flex text-7xl mb-2 font-mono">Practice Quiz Time!!!</h1>
<div class="mt-5">
<div class="mr-5">
<QuestionBlock question={answerChoicesAndQuestion[0][0]}, answerChoice1={answerChoicesAndQuestion[0][1]}, answerChoice2={answerChoicesAndQuestion[0][2]}, answerChoice3={answerChoicesAndQuestion[0][3]}, answerChoice4={answerChoicesAndQuestion[0][4]}/>
</div>
<div class="mr-28">
<QuestionBlock question={answerChoicesAndQuestion[1][0]}, answerChoice1={answerChoicesAndQuestion[1][1]}, answerChoice2={answerChoicesAndQuestion[1][2]}, answerChoice3={answerChoicesAndQuestion[1][3]}, answerChoice4={answerChoicesAndQuestion[1][4]}/>
</div>
<div class="mr-5">
<QuestionBlock question={answerChoicesAndQuestion[2][0]}, answerChoice1={answerChoicesAndQuestion[2][1]}, answerChoice2={answerChoicesAndQuestion[2][2]}, answerChoice3={answerChoicesAndQuestion[2][3]}, answerChoice4={answerChoicesAndQuestion[2][4]}/>
</div>
</div>
<p></p>
<div class="mt-8">
    <button on:click={() => showAnswers=true} class="text-white bg-gradient-to-br from-pink-500 to-orange-400 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-pink-200 dark:focus:ring-pink-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">Show Answers?</button>
</div>

{#if showAnswers}
    <p class="text-lg"> {answerString} </p>
{/if}

</div>
</div>
