<script>
    export let question;
    export let answerChoice1;
    export let answerChoice2;
    export let answerChoice3;
    export let answerChoice4;
    let correctAnswer = false
</script>

<div>
    <h1>{question}</h1>
    <div>
<label>
    <input type="radio" bind:group={correctAnswer} value={1}>{answerChoice1}
    <input type="radio" bind:group={correctAnswer} value={2}>{answerChoice2}
    <input type="radio" bind:group={correctAnswer} value={3}>{answerChoice3}
    <input type="radio" bind:group={correctAnswer} value={4}>{answerChoice4}
</label>
</div>
</div>
