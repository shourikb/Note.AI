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

<div class="bg-cover flex justify-center items-center w-screen h-screen" style="background-image: url('/src/lib/v602-nunoon-32-rippednotes.jpg'); height: 900px">
<div class="w-3/4 h-2/3 bg-white relative rounded-lg flex flex-col justify-center items-center border-sky-400 border-[18px]">
<h1 class="text-7xl">Choose a file upload type</h1>
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
    </div>
</div>
