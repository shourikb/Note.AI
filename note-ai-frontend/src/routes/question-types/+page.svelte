<script>
    let multipleChoice = false;
    let selectAll = false;
    let shortAnswer = false;
    let essay = false;
    let timer = false;
    let errorMessage = "We unfortunately do not support this functionality at this time";
</script>

<h1> What types of questions do you want </h1>
<label>
	<input type="checkbox" bind:checked={multipleChoice} />
    Multiple Choice
	<input type="checkbox" bind:checked={selectAll} />
    Select All the Apply
	<input type="checkbox" bind:checked={shortAnswer} />
    Short Answer
	<input type="checkbox" bind:checked={essay} />
    Essay
</label>
<label>
    <h2> Do you want a timer? </h2>
    <input type="radio" bind:group={timer} value={true} />
    yes
    <input type="radio" bind:group={timer} value={false}/>
    no
</label>
<label>
    <h3>Submit Choices</h3>
    <a href="/exam" target="_blank">
        <button disabled={!multipleChoice || selectAll || shortAnswer || essay || timer}>  Submit Choices</button>
    </a>

</label>

{#if selectAll || essay || shortAnswer || timer}
    <h3> {errorMessage} </h3>
{/if}
