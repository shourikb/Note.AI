<script>
    export var data;
	async function uploadFile(file) {
		console.log(file);
		const formData = new FormData();
		formData.append("sentFile", file);

		var response;
		try {
		response = await fetch("http://localhost:8000/polls/", {
			method: "POST",
			mode: "cors",
			body: formData,
			headers: {Accept: 'application/json', },
		});
		} catch (error) {
			console.log(error)
		}

		console.log(response);
		if (response.ok) {
			const data = await response.json();
			var text = data.question;
			console.log(text);
            console.log(data);
            return data;
		}
	}
	let files;

	$: if (files) {
		// Note that `files` is of type `FileList`, not an Array:
		// https://developer.mozilla.org/en-US/docs/Web/API/FileList
		console.log(files);

		for (const file of files) {
			data = uploadFile(file)
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
