<script>
    let multipleChoice = false;
    let selectAll = false;
    let shortAnswer = false;
    let essay = false;
    let timer = false;
    let errorMessage = "We unfortunately do not support this functionality at this time";
</script>

<div class="bg-cover flex justify-center items-center w-screen h-screen" style="background-image: url('/src/lib/v602-nunoon-32-rippednotes.jpg'); height: 900px">
<div class="w-3/4 h-2/3 bg-white relative rounded-lg flex flex-col justify-center items-center border-sky-400 border-[18px]">
<h1 class="text-5xl font-serif"> What types of questions do you want? </h1>
<div class= "flex flex-col pb-4 pt-4">
<label class="font-mono pb-2 pt-2">
	<input type="checkbox" bind:checked={multipleChoice} />
    Multiple Choice
</label>
<label class="font-mono pb-2 pt-2"> 
	<input type="checkbox" bind:checked={selectAll} />
    Select All the Apply
</label>
<label class="font-mono pb-2 pt-2">
	<input type="checkbox" bind:checked={shortAnswer} />
    Short Answer
</label>
<label class="font-mono pb-2 pt-2">
	<input type="checkbox" bind:checked={essay} />
    Essay
</label></div>
<label class="font-mono">
    <h2 class="text-3xl"> Do you want a timer? </h2>
    <div class = "flex justify-center items-center">
    <div class = "pb-2 pt-2 pr-4">
    <input type="radio" bind:group={timer} value={true} />
    Yes
    </div>
    <div class = "pb-2 pt-2 pl-4">
    <input type="radio" bind:group={timer} value={false} />
    No
    </div>
    </div>
</label>
<label class="font-sans">
    <h3></h3>
    <a href="/exam">
        <button disabled={!multipleChoice || selectAll || shortAnswer || essay || timer} class="justify-center
        mr-5 py-1 px-3 border-[1px]
        text-xs font-medium bg-white
        hover:bg-sky-200
        flex items-center">  Submit Choices</button>
    </a>
</label>
</div></div>


{#if selectAll || essay || shortAnswer || timer}
    <h3> {errorMessage} </h3>
{/if}

