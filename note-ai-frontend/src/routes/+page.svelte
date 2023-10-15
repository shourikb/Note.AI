<script>
    export var data;
    export var enabled = false;
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
            console.log(data);
            enabled = true;
            return enabled;
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
<h1 class="text-7xl font-serif flex">Choose a file upload type</h1>
<label for="avatar">
            <p class="mt-6 mb-6 text-2xl font-mono">
            Upload a Word Document:</p>
        </label>
<div class="items-center justify-center ml-32 flex font-bold">
<input accept=".docx" bind:files id="avatar" name="avatar" type="file" class="justify-center text-indigo-400
   file:mr-5 file:py-1 file:px-3 file:border-[1px]
   file:text-xs file:font-medium
   file:bg-stone-50 file:text-stone-700
   hover:file:cursor-pointer hover:file:bg-blue-50
   hover:file:text-blue-700
   flex items-center"/>
</div>

<div class="items-center justify-center mt-8 flex">
{#if files}
    <div class="mr-6">
	<h2 class="font-crazy">Selected files: </h2>
    </div>
    <div class="">
	{#each Array.from(files) as file}
        <div class="mb-5">
		<p>{file.name} ({file.size} bytes)</p>
        </div>
        {#await file.text() then text}
            {#if enabled}
            <div class="justify-center items-center">
            <a href="/question-types">
                <button class="justify-center items-center text-white bg-blue-700 hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300 font-medium rounded-full text-sm px-5 py-2.5 text-center mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Process Notes?</button>
            </a>
            </div>
            {:else}
                <p class="text-red-300">Loading...</p>

{/if}
        {/await}
	{/each}
    </div>
{/if}
                </div>
    </div>
</div>
