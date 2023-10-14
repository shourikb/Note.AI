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

<h1>Choose a file upload type</h1>

<label for="avatar">Upload a Word Document:</label>
<input accept=".docx, .doc" bind:files id="avatar" name="avatar" type="file" />

{#if files}
	<h2>Selected files:</h2>
	{#each Array.from(files) as file, i}
		<p>{file.name} ({file.size} bytes)</p>
        {#await file.text() then text}
            <p>e: {text} i: {i}</p>
        {/await}
	{/each}
{/if}
