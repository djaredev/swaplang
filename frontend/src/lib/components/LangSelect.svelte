<script lang="ts">
	let { options, value = $bindable() }: { options: string[]; value: string } = $props();
</script>

<select class="language-select" id="sourceLang" bind:value>
	{#each options as lang, i (i)}
		<option value={lang}>{lang}</option>
	{/each}
</select>

<style>
	.language-select {
		background: none;
		border: none;
		color: #1967d2;
		font-size: 14px;
		font-weight: 500;
		padding: 8px 12px;
		cursor: pointer;
		border-radius: 4px;
		transition: background-color 0.2s;
		outline: none;
	}

	.language-select:hover {
		background-color: #f1f3f4;
	}

	.language-select:focus {
		background-color: #e8f0fe;
	}

	.language-select option {
		background: white;
		color: #202124;
		padding: 8px;
	}
</style>
