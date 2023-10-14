<script>
	let files;

	$: if (files) {
		// Note that `files` is of type `FileList`, not an Array:
		// https://developer.mozilla.org/en-US/docs/Web/API/FileList
		console.log(files);

		for (const file of files) {
			console.log(`${file.name}: ${file.size} bytes`);
		}
	}
</script>

<h1 class="text-3xl">Choose a file upload type</h1>
<label for="avatar">Upload a Word Document:</label>
<input accept=".txt,.doc,.docx,.xml,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document" bind:files id="avatar" name="avatar" type="file" />

{#if files}
	<h2>Selected files:</h2>
	{#each Array.from(files) as file}
		<p>{file.name} ({file.size} bytes)</p>
        {#await file.text() then text}
            <a href="/question-types">
                <button>Process Notes?</button>
            </a>
        {/await}
	{/each}
{/if}
