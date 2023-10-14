<script>
    let multipleChoice = false;
    let selectAll = false;
    let shortAnswer = false;
    let essay = false;
    let timer = false;
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
    <a href="/exam"><button disabled={!multipleChoice && selectAll && essay && timer}> <a href="/exam"> Submit Choices</button>
</label>

{#if selectAll}
	<p>We unfortunately do not support this functionality at this time</p>
    {:else}
    <p></p>
{/if}

{#if shortAnswer}
	<p>We unfortunately do not support this functionality at this time</p>
    {:else}
    <p></p>
{/if}

{#if essay}
	<p>We unfortunately do not support this functionality at this time</p>
    {:else}
    <p></p>
{/if}

{#if timer}
	<p>We unfortunately do not support this functionality at this time</p>
    {:else}
    <p></p>
{/if}
