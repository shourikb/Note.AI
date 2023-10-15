<script>
    export let question;
    export let answerChoice1;
    export let answerChoice2;
    export let answerChoice3;
    export let answerChoice4;
    let correctAnswer = false
</script>

<div class="">
    <h1 class="text-3xl mt-10 mb-2">{question.slice(0,-1)}</h1>
    <div class="flex text-xl">
<label>
    <div class="mb-1 mt-1">
                <input type="radio" bind:group={correctAnswer} value={1}>{" " + answerChoice1.slice(0,-1)}
                </div>
    <div>
                <input type="radio" bind:group={correctAnswer} value={2}>{" " + answerChoice2.slice(0,-1)}
                </div>
                <div>
                <input type="radio" bind:group={correctAnswer} value={3}>{" " + answerChoice3.slice(0,-1)}
                </div>
                <div>
                <input type="radio" bind:group={correctAnswer} value={4}>{" " + answerChoice4}
                </div>
</label>
</div>
</div>
